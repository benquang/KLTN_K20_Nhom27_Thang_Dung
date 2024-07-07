import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { LeagueComponent } from './league/league.component';
import { KetQuaComponent } from './ket-qua/ket-qua.component';
import { UpcomingTranDauComponent } from './upcoming-tran-dau/upcoming-tran-dau.component';
import { LichThiDauComponent } from './lich-thi-dau/lich-thi-dau.component';
import { ThongSoTranDauComponent } from './thong-so-tran-dau/thong-so-tran-dau.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'leagues', component: LeagueComponent },
  { path: 'ket-qua/:league/:season', component: KetQuaComponent },
  { path: 'lich-thi-dau/:league', component: LichThiDauComponent },

  { path: 'tran-dau/:match', component: ThongSoTranDauComponent },
  { path: 'upcoming/:match', component: UpcomingTranDauComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }