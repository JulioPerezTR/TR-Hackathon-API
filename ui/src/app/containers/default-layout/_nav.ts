import { INavData } from '@coreui/angular';

export const navItems: INavData[] = [
  {
    title: true,
    name: 'General Dashboards'
  },
  {
    name: 'Dashboard',
    url: '/dashboard',
    iconComponent: { name: 'cil-speedometer' }
  },
  {
    name: 'Timeline',
    url: '/general/timelines',
    iconComponent: { name: 'cil-chart-line' }
  },
  {
    name: 'Countries',
    url: '/general/countries',
    iconComponent: { name: 'cil-globe-alt' }
  }
];
