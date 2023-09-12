import { Component, OnInit } from '@angular/core';
import { UntypedFormControl, UntypedFormGroup } from '@angular/forms';

import { DashboardChartsData, IChartProps } from './dashboard-charts-data';

@Component({
  templateUrl: 'dashboard.component.html',
  styleUrls: ['dashboard.component.scss']
})
export class DashboardComponent implements OnInit {

  constructor(private chartsData: DashboardChartsData) { }

  public mainChart: IChartProps = {};
  public chart: Array<IChartProps> = [];
  public averageRadioGroup = new UntypedFormGroup({
    averageRadio: new UntypedFormControl('Average')
  });

  ngOnInit(): void {
    this.mainChart = this.chartsData.mainChart;
  }

  setTypeData(value: string): void {
    this.averageRadioGroup.setValue({ averageRadio: value });
    this.chartsData.initMainChart(value);
    this.mainChart = this.chartsData.mainChart;
  }
}
