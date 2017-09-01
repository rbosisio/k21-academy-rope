import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-welcome',
  templateUrl: './welcome.component.html',
  styleUrls: ['./welcome.component.scss']
})
export class WelcomeComponent implements OnInit {
  logoUrl: string = './assets/images/logo-rope.jpg';
  logoTitle: string = 'Instituto Rope'

  constructor() { }

  ngOnInit() {
  }

}
