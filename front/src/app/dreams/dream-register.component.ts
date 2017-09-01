import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators  } from '@angular/forms'
import { Http } from '@angular/http';

@Component({
  selector: 'app-dream-register',
  templateUrl: './dream-register.component.html',
  styleUrls: ['./dream-register.component.scss']
})
export class DreamRegisterComponent {
  
  registerDreamUrl: string = "http://sonhos.institutorope.com.br:8000/api/dreams/";
  
  formSubmitted: boolean = false;
  registerFormFieldValid: {} = {};
  registerForm:FormGroup = new FormGroup({
    name: new FormControl('', Validators.required),
    age: new FormControl('', Validators.required),
    email: new FormControl('', Validators.required),
    phone: new FormControl('', Validators.required),
    address: new FormControl('', Validators.required),
    contact_name: new FormControl('', Validators.required),
    liason: new FormControl('', Validators.required),
    inmate: new FormControl(false, Validators.required),
    hospital_name: new FormControl(),
    hospital_contact: new FormControl(),
    medical_approved: new FormControl(false, Validators.required),
    parental_approved: new FormControl(false, Validators.required),
    description: new FormControl('', Validators.required),
    hospital_address: new FormControl('', Validators.required),
    observation: new FormControl('', Validators.required),
    planning_description: new FormControl('', Validators.required),
    health_conditions: new FormControl('', Validators.required),
    dream_report: new FormControl('', Validators.required)
  });

  constructor(private http: Http) { }

  onFormSubmit(): void {
    this.formSubmitted = true;

    let formObj = this.registerForm.getRawValue();

    let serializedForm = JSON.stringify(formObj);

    this.http.post(this.registerDreamUrl, serializedForm)
    .subscribe(
        data => console.log("success!", data),
        error => console.error("couldn't post because", error)
    );
  } 

}
