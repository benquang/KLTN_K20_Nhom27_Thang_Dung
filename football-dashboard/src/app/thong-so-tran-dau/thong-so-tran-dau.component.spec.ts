import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ThongSoTranDauComponent } from './thong-so-tran-dau.component';

describe('ThongSoTranDauComponent', () => {
  let component: ThongSoTranDauComponent;
  let fixture: ComponentFixture<ThongSoTranDauComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ThongSoTranDauComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ThongSoTranDauComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
