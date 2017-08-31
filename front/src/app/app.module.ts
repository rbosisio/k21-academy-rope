import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http'
import { RouterModule } from '@angular/router'
import { FormsModule } from "@angular/forms";

import { AppComponent } from './app.component';
import { WelcomeComponent } from './home/welcome.component';
import { DreamRegisterModule } from "./dreams/dream-register.module";

@NgModule({
  declarations: [
    AppComponent,
    WelcomeComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    RouterModule.forRoot([
      { path: 'welcome', component: WelcomeComponent },
      { path: '', redirectTo: 'welcome', pathMatch: 'full'},
      { path: '**', redirectTo: 'welcome', pathMatch: 'full'}
    ]),
    DreamRegisterModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
