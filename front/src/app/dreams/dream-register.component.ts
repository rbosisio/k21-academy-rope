import { Component } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms'
import { Http } from '@angular/http';

@Component({
  selector: 'app-dream-register',
  templateUrl: './dream-register.component.html',
  styleUrls: ['./dream-register.component.scss']
})
export class DreamRegisterComponent {

  registerForm:FormGroup = new FormGroup({
    name: new FormControl(),
    age: new FormControl(),
    email: new FormControl(),
    phone: new FormControl(),
    address: new FormControl(),
    contact_name: new FormControl(),
    liason: new FormControl(),
    inmate: new FormControl(),
    hospital_name: new FormControl(),
    hospital_contact: new FormControl(),
    medical_approved: new FormControl(),
    parental_approved: new FormControl(),
    description: new FormControl(),
    hospital_address: new FormControl(),
    observation: new FormControl(),
    status: new FormControl(),
    planning_description: new FormControl(),
    health_conditions: new FormControl(),
    dream_report: new FormControl()
  }); 
  
  constructor(private http: Http) { }

  onFormSubmit(): void {
    let formObj = this.registerForm.getRawValue();
    formObj.inmate = false; 
    formObj.medical_approved = true; 
    formObj.parental_approved = true;

    let serializedForm = JSON.stringify(formObj);

    this.http.post("http://sonhos.institutorope.com.br:8000/api/dreams/", serializedForm)
    .subscribe(
        data => console.log("success!", data),
        error => console.error("couldn't post because", error)
    );
  } 

}
