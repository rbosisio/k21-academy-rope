import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators  } from '@angular/forms'
import { Http } from '@angular/http';

@Component({
  selector: 'app-dream-register',
  templateUrl: './dream-register.component.html',
  styleUrls: ['./dream-register.component.scss']
})
export class DreamRegisterComponent {
  
  registerDreamUrl: string = "http://admin.institutorope.com.br/api/dreams/";
  //registerDreamUrl: string = "http://localhost:8000/api/dreams/";
  
  fieldsRequiredMessage: string = "Preecha todos os campos obrigatórios.";
  errorMessage: string = "Ocorreu um erro no cadastro do sonho. Por favor tente novamente ou entre em contanto conosco.";
  successMessage: string = "Sonho cadastrado com sucesso! Entraremos em contato em breve!";

  formSubmitted: boolean = false;
  success: boolean = false;
  failed: boolean = false;
  registerFormFieldValid: {} = {};
  registerForm:FormGroup = new FormGroup({
    dreamer_name: new FormControl('', Validators.required),
    dreamer_age: new FormControl('', Validators.required),
    dreamer_address: new FormControl('', Validators.required),
    dreamer_health_conditions: new FormControl('', Validators.required),
    contact_name: new FormControl('', Validators.required),
    contact_email: new FormControl('', Validators.required),
    contact_phone: new FormControl('', Validators.required),
    contact_liason: new FormControl('', Validators.required),
    inmate: new FormControl(false, Validators.required),
    local: new FormControl(''),
    local_name: new FormControl(''),
    local_address: new FormControl(''),
    local_phone: new FormControl(''),
    medical_approved: new FormControl(false, Validators.required),
    parental_approved: new FormControl(false, Validators.required),
    description: new FormControl('', Validators.required),
    planning_description: new FormControl(''),
    dream_needs: new FormControl(''),
    needs_attended: new FormControl(''),
    status: new FormControl(),
    category: new FormControl()
  });

  constructor(private http: Http) { }

  onFormSubmit(): void {
    this.formSubmitted = true;
    let formObj = this.registerForm.getRawValue();
    let serializedForm = JSON.stringify(formObj);
  
    console.log(formObj);
    window.scrollTo(0,0);

    if(this.registerForm.valid){
      this.http.post(this.registerDreamUrl, serializedForm)
      .subscribe(
          data => {
            console.log("success!", data);
            this.success = true;
          },
          error => {
            this.failed = true;
            console.error("couldn't post because", error);
          }
      );
    }
  } 

}
