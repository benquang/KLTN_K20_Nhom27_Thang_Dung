import { Routes } from '@angular/router';
import { SystemConstant } from '@constants/system.constant';

import { HomeComponent } from './home/home.component';

export const routes: Routes = [
  {
    path: '',
    component: HomeComponent,
    title: `Kết quả | ${SystemConstant.WEB_NAME}`,
  },
];
