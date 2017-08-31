import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DreamRegisterComponent } from './dream-register.component';

describe('DreamRegisterComponent', () => {
  let component: DreamRegisterComponent;
  let fixture: ComponentFixture<DreamRegisterComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DreamRegisterComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DreamRegisterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
