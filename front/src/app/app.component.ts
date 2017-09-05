import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  styleUrls: ['./app.component.scss'],
  template: `
  	<header class="main-header">
  		<div class="top-bar"></div>
  		<div class='container'>
			<a href="http://institutorope.com.br/">
				<img src="../../assets/images/logo-header.png" alt="" class="logo">
			</a>

			<ul>
				<li><a href="http://institutorope.com.br/" target="_blank">Home</a></li>
				<li><a href="#">Instituto Rope</a></li>
				<li><a href="#">Sonhos</a></li>
				<li><a href="#">Parceiros</a></li>
				<li><a href="#">Como Apoiar</a></li>
				<li><a href="#">Fale Conosco</a></li>
			</ul>
		</div>
	</header>

    <div class='container'>
      <router-outlet></router-outlet>
    </div>`
})
export class AppComponent {
  title = 'app';
}
