import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DreamListComponent } from './dream-list.component';

describe('DreamListComponent', () => {
  let component: DreamListComponent;
  let fixture: ComponentFixture<DreamListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DreamListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DreamListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
