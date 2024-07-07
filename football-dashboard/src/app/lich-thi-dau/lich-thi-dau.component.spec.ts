import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LichThiDauComponent } from './lich-thi-dau.component';

describe('LichThiDauComponent', () => {
  let component: LichThiDauComponent;
  let fixture: ComponentFixture<LichThiDauComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [LichThiDauComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(LichThiDauComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
