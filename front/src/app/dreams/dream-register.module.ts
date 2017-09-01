import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { HttpModule } from '@angular/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { DreamRegisterComponent } from "./dream-register.component";

@NgModule({
  imports: [
    CommonModule,    
    FormsModule,
    ReactiveFormsModule,
    HttpModule,
    RouterModule.forChild([
      { path: 'cadastro', component: DreamRegisterComponent }  
    ]),
  ],
  declarations: [
    DreamRegisterComponent
  ]
})
export class DreamRegisterModule { }
