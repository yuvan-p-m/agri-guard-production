$adb = "C:\Users\kevin\AppData\Local\Android\Sdk\platform-tools\adb.exe"
$apk = "C:\Users\kevin\Documents\sih-agri-smart\frontend-repo\android\app\build\outputs\apk\debug\app-debug.apk"
$pkg = "com.agri.app"
$activity = "com.agri.app.MainActivity"

Write-Host "=== AgriGuard USB Device Auto-Installer ==="
Write-Host "Watching for Android device via ADB..."

$maxAttempts = 150
$attempts = 0

while ($attempts -lt $maxAttempts) {
    $lines = & $adb devices
    $found = $false
    foreach ($line in $lines) {
        $trimmed = $line.Trim()
        if ($trimmed -and -not ($trimmed -match "^List of")) {
            if ($trimmed -match "^([^\s]+)\s+device$") {
                $devId = $matches[1]
                Write-Host ">> Active device connected: $devId"
                
                Write-Host ">> Setting up USB reverse proxy for backend (tcp:8000) and frontend (tcp:5173)..."
                & $adb -s $devId reverse tcp:8000 tcp:8000
                & $adb -s $devId reverse tcp:5173 tcp:5173

                Write-Host ">> Installing AgriGuard debug APK..."
                & $adb -s $devId install -r $apk

                Write-Host ">> Launching AgriGuard ($pkg)..."
                & $adb -s $devId shell am start -n "$pkg/$activity"

                Write-Host ">> SUCCESS! AgriGuard is now running on $devId."
                exit 0
            } elseif ($trimmed -match "^([^\s]+)\s+unauthorized$") {
                $devId = $matches[1]
                Write-Host ">> Device detected ($devId) but UNAUTHORIZED. Please tap 'Allow USB debugging' on your phone screen."
                $found = $true
            }
        }
    }
    Start-Sleep -Seconds 2
    $attempts++
}

Write-Host "Timeout waiting for device. Please check USB debugging."
exit 1
