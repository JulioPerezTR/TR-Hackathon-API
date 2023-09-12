import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { TimelinesComponent } from './timelines.component';
import { CountriesComponent } from './countries.component';

const routes: Routes = [
  {
    path: '',
    data: {
      title: 'General',
    },
    children: [
      {
        path: '',
        pathMatch: 'full',
        redirectTo: 'timelines',
      },
      {
        path: 'timelines',
        component: TimelinesComponent,
        data: {
          title: 'Timelines',
        },
      },
      {
        path: 'countries',
        component: CountriesComponent,
        data: {
          title: 'Countries',
        },
      },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class GeneralRoutingModule {}
