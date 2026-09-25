import React from 'react';
import { FieldDataTab, type FieldDataTabProps } from './FieldDataTab';

export interface IoTSensorsTabProps extends FieldDataTabProps {}

export const IoTSensorsTab: React.FC<IoTSensorsTabProps> = (props) => {
  return <FieldDataTab {...props} />;
};

export default IoTSensorsTab;
