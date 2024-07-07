import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NZ_I18N } from 'ng-zorro-antd/i18n';
import { en_US } from 'ng-zorro-antd/i18n';
import { registerLocaleData } from '@angular/common';
import en from '@angular/common/locales/en';
import { FormsModule } from '@angular/forms';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { provideHttpClient } from '@angular/common/http';
import { TestComponent } from './test/test.component';

import { NzLayoutModule } from 'ng-zorro-antd/layout';
import { NzMenuModule } from 'ng-zorro-antd/menu';  
import { NzGridModule } from 'ng-zorro-antd/grid';
import { NzTableModule } from 'ng-zorro-antd/table';

import { HomeComponent } from './home/home.component';
import { TinTucComponent } from './home/tin-tuc/tin-tuc.component';
import { CardNewsBigComponent } from './home/card-news-big/card-news-big.component';
import { CardNewsSmallComponent } from './home/card-news-small/card-news-small.component';
import { LeagueComponent } from './league/league.component';
import { KetQuaComponent } from './ket-qua/ket-qua.component';
import { UpcomingTranDauComponent } from './upcoming-tran-dau/upcoming-tran-dau.component';
import { LichThiDauComponent } from './lich-thi-dau/lich-thi-dau.component';
import { ThongSoTranDauComponent } from './thong-so-tran-dau/thong-so-tran-dau.component';

registerLocaleData(en);

@NgModule({
  declarations: [
    AppComponent,
    TestComponent,

    HomeComponent,
    TinTucComponent,
    CardNewsBigComponent,
    CardNewsSmallComponent,
    LeagueComponent,
    KetQuaComponent,
    UpcomingTranDauComponent,
    LichThiDauComponent,
    ThongSoTranDauComponent,

    

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    NzLayoutModule,
    NzMenuModule,
    NzGridModule,
    NzTableModule
  ],
  providers: [
    provideClientHydration(),
    { provide: NZ_I18N, useValue: en_US },
    provideAnimationsAsync(),
    provideHttpClient()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
