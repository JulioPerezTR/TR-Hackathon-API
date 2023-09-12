import { Injectable } from '@angular/core';
import { getStyle } from '@coreui/utils';

export interface IChartProps {
  data?: any;
  labels?: any;
  options?: any;
  colors?: any;
  type?: any;
  legend?: any;

  [propName: string]: any;
}

@Injectable({
  providedIn: 'any'
})
export class DashboardChartsData {
  constructor() {
    this.initMainChart();
  }

  public mainChart: IChartProps = {};

  initMainChart(dataType: string = 'Average') {
    const brandSuccess = getStyle('--cui-success') ?? '#4dbd74';
    const brandInfo = getStyle('--cui-info') ?? '#20a8d8';
    const brandDanger = getStyle('--cui-danger') || '#f86c6b';
    const brandPrimary = getStyle('--cui-primary') || '#321fdb';
    const brandWarning = getStyle('--cui-warning') || '#FFCE56';
    const brandSecondary = getStyle('--cui-secondary') || 'rgba(220, 220, 220, 0.2)';

    // mainChart
    // mainChart
    this.mainChart['elements'] = 16;
    
    if (dataType === 'Min') {
      this.mainChart['Data2'] = [
        1.0,
        1.0,
        1.0,
        1.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ]
      this.mainChart['Data3'] = [
        1.0,
        1.0,
        1.0,
        1.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ];
      this.mainChart['Data4'] = [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ];
      this.mainChart['Data5'] = [
        1.0,
        1.0,
        1.0,
        1.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ];
      this.mainChart['Data6'] = [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ];
      this.mainChart['Data7'] = [
        1.0,
        1.0,
        1.0,
        1.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ];
    }
    else if (dataType == 'Max') {
      this.mainChart['Data2'] = [
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0
    ];
      this.mainChart['Data3'] = [
        5.0,
        4.5,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0
    ];
      this.mainChart['Data4'] = [
        0.0,
        0.0,
        0.0,
        0.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0
    ];
      this.mainChart['Data5'] = [
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0
    ];
      this.mainChart['Data6'] = [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        5.0,
        5.0,
        5.0,
        5.0
    ];
      this.mainChart['Data7'] = [
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0,
        5.0
    ];
    }
    else {
      this.mainChart['Data2'] = [
        2.9285714285714284,
        2.822429906542056,
        2.8376068376068377,
        2.7777777777777777,
        2.7480916030534353,
        2.4992481203007517,
        2.3469184890656063,
        2.3351519875292284,
        2.4972332015810275,
        2.569028487947407,
        2.730802415875755,
        2.50996015936255,
        3.2497839239412274,
        2.8819188191881917,
        2.8940828402366865,
        3.197592778335005
    ];
      this.mainChart['Data3'] = [
        3.0714285714285716,
        2.9766355140186915,
        2.8653846153846154,
        2.95679012345679,
        2.851145038167939,
        2.750375939849624,
        2.7157057654075545,
        2.7022603273577555,
        2.7367588932806326,
        2.8714390065741418,
        3.0025884383088868,
        2.8217131474103585,
        3.2515125324114087,
        2.984317343173432,
        3.050887573964497,
        3.270812437311936
    ];
      this.mainChart['Data4'] = [
        0.0,
        0.0,
        0.0,
        0.0,
        2.33587786259542,
        3.130827067669173,
        3.002982107355865,
        3.043647700701481,
        3.1209486166007907,
        3.3360116873630385,
        3.439171699741156,
        3.196215139442231,
        3.6248919619706137,
        3.305350553505535,
        3.3319526627218936,
        3.546639919759278
    ];
      this.mainChart['Data5'] = [
        3.2738095238095237,
        3.322429906542056,
        3.2286324786324787,
        3.162037037037037,
        3.0543893129770994,
        2.9744360902255638,
        2.8986083499005963,
        2.8074824629773967,
        2.8197628458498025,
        3.065010956902849,
        3.1104400345125107,
        3.0139442231075697,
        3.3171996542783058,
        3.0332103321033212,
        3.0568047337278106,
        3.3400200601805414
    ];
      this.mainChart['Data6'] = [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.996542783059637,
        3.375461254612546,
        3.3893491124260353,
        3.661985957873621
    ];
      this.mainChart['Data7'] = [
        3.732142857142857,
        3.822429906542056,
        3.7948717948717947,
        3.837962962962963,
        3.529580152671756,
        3.4842105263157896,
        3.3508946322067596,
        3.2915042868277475,
        3.38498023715415,
        3.547845142439737,
        3.5798101811906817,
        3.3814741035856573,
        3.6162489196197063,
        3.284132841328413,
        3.342603550295858,
        3.6318956870611836
    ];
    }

    let labels: string[] = [
      "2008",
      "2009",
      "2010",
      "2011",
      "2012",
      "2013",
      "2014",
      "2015",
      "2016",
      "2017",
      "2018",
      "2019",
      "2020",
      "2021",
      "2022",
      "2023"
  ];

    const colors = [
      {
        backgroundColor: 'transparent',
        borderColor: brandSuccess,
        pointHoverBackgroundColor: '#fff'
      },
      {
        backgroundColor: 'transparent',
        borderColor: brandInfo,
        pointHoverBackgroundColor: '#fff'
      },
      {
        backgroundColor: 'transparent',
        borderColor: brandDanger,
        pointHoverBackgroundColor: '#fff',
      },
      {
        backgroundColor: 'transparent',
        borderColor: brandPrimary,
        pointHoverBackgroundColor: '#fff'
      },
      {
        backgroundColor: 'transparent',
        borderColor: brandWarning,
        pointHoverBackgroundColor: '#fff'
      },
      {
        backgroundColor: 'transparent',
        borderColor: brandSecondary,
        pointHoverBackgroundColor: '#fff',
      }
    ];

    const datasets = [
      {
        data: this.mainChart['Data2'],
        label: 'Average Senior Leadership per year',
        ...colors[1]
      },
      {
        data: this.mainChart['Data3'],
        label: 'Average Culture & Values per year',
        ...colors[2]
      },
      {
        data: this.mainChart['Data3'],
        label: 'Average Compensation & Benefits per year',
        ...colors[3]
      },
      {
        data: this.mainChart['Data3'],
        label: 'Average Diversity & Inclusion per year',
        ...colors[4]
      },
      {
        data: this.mainChart['Data3'],
        label: 'Average Work-Life Balance per yearr',
        ...colors[5]
      }
    ];

    const plugins = {
      legend: {
        display: false
      },
      tooltip: {
        callbacks: {
          labelColor: function(context: any) {
            return {
              backgroundColor: context.dataset.borderColor
            };
          }
        }
      }
    };

    const options = {
      maintainAspectRatio: false,
      plugins,
      scales: {
        x: {
          grid: {
            drawOnChartArea: false
          }
        },
        y: {
          beginAtZero: true,
          max: 6,
          ticks: {
            maxTicksLimit: 5,
            stepSize: Math.ceil(250 / 5)
          }
        }
      },
      elements: {
        line: {
          tension: 0.4
        },
        point: {
          radius: 0,
          hitRadius: 10,
          hoverRadius: 4,
          hoverBorderWidth: 3
        }
      }
    };

    this.mainChart.type = 'line';
    this.mainChart.options = options;
    this.mainChart.data = {
      datasets,
      labels
    };
  }

}
