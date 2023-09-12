import { Component, OnInit } from '@angular/core';
import { GeneralService } from './../../services/general.service';
import { ResponseData } from 'src/app/models/responseData.model';

@Component({
  templateUrl: 'timelines.component.html'
})
export class TimelinesComponent implements OnInit {

  constructor(
    private generalService: GeneralService
  ){}

  graphicNames: Array<string> = [];
  graphicAverages: Array<number> = [];
  index = 0;

  data: any[] = [];


  ngOnInit(): void {
    this.generalService.getCardsData().subscribe((metrics: Array<ResponseData>) => {
      if (!!metrics) {
        metrics.forEach((metric, index) => {
          this.graphicNames.push(metric.title);
          this.graphicAverages.push(metric.average);

          this.data[index] = {
            labels: metric.x,
            datasets: [{
              label: metric.title,
              backgroundColor: '#f87979',
              data: metric.y
            }]
          }

          this.index++;
        })
      }
    });
  }
   
}


