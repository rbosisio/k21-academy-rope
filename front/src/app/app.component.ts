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
				<li><a href="http://institutorope.com.br/">Home</a></li>
				<li><a href="http://institutorope.com.br/quem-somos/">Quem Somos</a></li>
				<li><a href="http://institutorope.com.br/sonhos-realizados/">Sonhos Realizados</a></li>
				<li><a href="http://institutorope.com.br/parceiros/">Parceiros</a></li>
				<li><a href="http://sonhos.institutorope.com.br/adote-um-sonho">Como Apoiar</a></li>
				<li><a href="http://institutorope.com.br/fale-conosco/">Fale Conosco</a></li>
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
