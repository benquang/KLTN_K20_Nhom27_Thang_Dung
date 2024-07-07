import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UpcomingTranDauComponent } from './upcoming-tran-dau.component';

describe('UpcomingTranDauComponent', () => {
  let component: UpcomingTranDauComponent;
  let fixture: ComponentFixture<UpcomingTranDauComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [UpcomingTranDauComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(UpcomingTranDauComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
