import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from "@angular/forms";

import { PartnerRegisterComponent } from './partner-register.component';
import { HttpModule } from "@angular/http";
import { RouterModule } from "@angular/router";

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    HttpModule,
    RouterModule.forChild([
      { path: 'cadastro-parceiro', component: PartnerRegisterComponent}  
    ])
  ],
  declarations: [PartnerRegisterComponent]
})
export class PartnerModule { }
