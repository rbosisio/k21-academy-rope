import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { VoluntaryRegisterComponent } from './voluntary-register.component';

describe('VoluntaryRegisterComponent', () => {
  let component: VoluntaryRegisterComponent;
  let fixture: ComponentFixture<VoluntaryRegisterComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ VoluntaryRegisterComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(VoluntaryRegisterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
