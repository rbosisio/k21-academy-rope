import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { HttpModule } from '@angular/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { DreamRegisterComponent } from "./dream-register.component";
import { DreamListComponent } from './dream-list.component';

@NgModule({
  imports: [
    CommonModule,    
    FormsModule,
    ReactiveFormsModule,
    HttpModule,
    RouterModule.forChild([
      { path: 'cadastro', component: DreamRegisterComponent },
      { path: 'adote-um-sonho', component: DreamListComponent },
    ])
  ],
  declarations: [
    DreamRegisterComponent,
    DreamListComponent
  ]
})
export class DreamModule { }
