import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { HttpModule } from '@angular/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MultiselectDropdownModule } from 'angular-2-dropdown-multiselect';

import { VoluntaryRegisterComponent } from './voluntary-register.component';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    HttpModule,
    MultiselectDropdownModule,
    RouterModule.forChild([
      { path: 'cadastro-voluntario', component: VoluntaryRegisterComponent}  
    ])
  ],
  declarations: [
  	VoluntaryRegisterComponent
  ]
})
export class VoluntaryModule { }
