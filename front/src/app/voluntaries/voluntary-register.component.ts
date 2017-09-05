import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators  } from '@angular/forms'
import { Http } from '@angular/http';

@Component({
  selector: 'app-voluntary-register',
  templateUrl: './voluntary-register.component.html',
  styleUrls: ['./voluntary-register.component.scss']
})
export class VoluntaryRegisterComponent {

  registerVoluntaryUrl: string = "http://admin.institutorope.com.br/api/voluntaries/";

  formSubmitted: boolean = false;
  registerFormFieldValid: {} = {};
  registerForm:FormGroup = new FormGroup({
    name: new FormControl('', Validators.required),
    nickname: new FormControl('', Validators.required),
    birthdate: new FormControl('', Validators.required),
    telephone: new FormControl('', Validators.required),
    cellphone: new FormControl('', Validators.required),
    email: new FormControl('', Validators.required),
    address: new FormControl('', Validators.required),
    personal_characteristics: new FormControl('', Validators.required),
    talents: new FormControl('', Validators.required)
  });

  constructor(private http: Http) { }

  onFormSubmit(): void {
    this.formSubmitted = true;

    let formObj = this.registerForm.getRawValue();

    let serializedForm = JSON.stringify(formObj);

    this.http.post(this.registerVoluntaryUrl, serializedForm)
    .subscribe(
        data => console.log("success!", data),
        error => console.error("couldn't post because", error)
    );
  }

}
