import {
  AfterContentInit,
  ChangeDetectorRef,
  Component,
  OnInit
} from '@angular/core';
  import { getStyle } from '@coreui/utils';
import { GeneralService } from './../../../services/general.service';
import { ResponseData } from 'src/app/models/responseData.model';

@Component({
  selector: 'app-widgets-dropdown',
  templateUrl: './widgets-dropdown.component.html',
  styleUrls: ['./widgets-dropdown.component.scss']
})
export class WidgetsDropdownComponent implements OnInit, AfterContentInit {

  constructor(
    private changeDetectorRef: ChangeDetectorRef,
    private generalService: GeneralService
  ) {}

  graphicNames: Array<string> = [];
  graphicAverages: Array<number> = [];
  graphicColors = ['primary', 'success', 'info', 'dark', 'warning', 'danger'];
  index = 0;

  data: any[] = [];
  options: any[] = [];
  optionsDefault = {
    plugins: {
      legend: {
        display: false
      }
    },
    maintainAspectRatio: false,
    scales: {
      x: {
        grid: {
          display: false,
          drawBorder: false
        },
        ticks: {
          display: false
        }
      },
      y: {
        display: false,
        grid: {
          display: false
        },
        ticks: {
          display: false
        }
      }
    },
    elements: {
      line: {
        borderWidth: 1,
        tension: 0.4
      }
    }
  };

  ngOnInit(): void {
    this.generalService.getCardsData().subscribe((metrics: Array<ResponseData>) => {
      if (!!metrics) {
        metrics.forEach((metric, index) => {
          this.graphicNames.push(metric.title);
          this.graphicAverages.push(metric.average);
          const [minValue, maxValue] = this.getMaxMin(metric.y);
          const dotColor = `--cui-${this.graphicColors[this.index % this.graphicColors.length]}`;

          this.data[index] = {
            labels: metric.x,
            datasets: [{
              borderColor: 'rgba(255,255,255,.55)',
              pointBackgroundColor: getStyle(dotColor),
              pointHoverBorderColor: getStyle(dotColor),
              data: metric.y
            }]
          }

          this.setOptions(minValue, maxValue);
          this.index++;
        })
      }
    });
  }

  getMaxMin(values: Array<number>) {
    let min: number = Number.MAX_VALUE;
    let max: number = Number.MIN_VALUE;

    values?.forEach((data) => {
      if (data < min) {
        min = data;
      }
      if (data > max) {
        max = data;
      }
    })

    return [min - 1, max + 1];
  }

  ngAfterContentInit(): void {
    this.changeDetectorRef.detectChanges();
  }

  setOptions(min: number, max: number) {
    const options = JSON.parse(JSON.stringify(this.optionsDefault));
    options.scales.y.min = min;
    options.scales.y.max = max;
    this.options.push(options);
  }
}
