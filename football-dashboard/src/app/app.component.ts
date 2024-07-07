import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'final-front-end-2';

  isResponsive = false;

  toggleResponsive() {
    this.isResponsive = !this.isResponsive;
  }

  
}
