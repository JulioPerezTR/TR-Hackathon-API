import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';

import { CardModule, GridModule, NavModule, UtilitiesModule, TabsModule } from '@coreui/angular';
import { IconModule } from '@coreui/icons-angular';
import { ChartjsModule } from '@coreui/angular-chartjs';

import { TimelinesComponent } from './timelines.component';
import { CountriesComponent } from './countries.component';

// General Routing
import { GeneralRoutingModule } from './general-routing.module';

@NgModule({
  imports: [
    CommonModule,
    GeneralRoutingModule,
    CardModule,
    GridModule,
    UtilitiesModule,
    IconModule,
    NavModule,
    TabsModule,
    ChartjsModule
  ],
  declarations: [
    TimelinesComponent,
    CountriesComponent
  ]
})
export class GeneralModule {
}
