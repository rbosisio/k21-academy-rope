import { Component, OnInit } from '@angular/core';
import { Http } from "@angular/http";
import { Router } from "@angular/router";
import { FormGroup, FormControl, Validators  } from '@angular/forms'
import { IMultiSelectOption, IMultiSelectSettings } from "angular-2-dropdown-multiselect";

@Component({
  selector: 'app-partner-register',
  templateUrl: './partner-register.component.html',
  styleUrls: ['./partner-register.component.scss']
})
export class PartnerRegisterComponent implements OnInit {

  registerPartnerUrl: string = "http://admin.institutorope.com.br/api/partners/";
  
  fieldsRequiredMessage: string = "Preecha todos os campos obrigatórios.";
  errorMessage: string = "Ocorreu um erro no seu cadastro. Por favor tente novamente ou entre em contanto conosco.";
  successMessage: string = "Seu cadastrado como parceiro foi realizado com sucesso! Entraremos em contato em breve!";
  
  success: boolean = false;
  failed: boolean = false;
  formSubmitted: boolean = false;
  registerForm:FormGroup = new FormGroup({
    document_type: new FormControl('', Validators.required),
    contact_name: new FormControl('', Validators.required),
    company_name: new FormControl(''),
    document: new FormControl(''),
    telephone: new FormControl(''),
    cellphone: new FormControl('', Validators.required),
    address: new FormControl(''),
    has_specific_dream: new FormControl(Validators.required),
    money_help: new FormControl('', Validators.required),
    service_help: new FormControl('', Validators.required),
    help_description: new FormControl('', Validators.required),
    observation: new FormControl('', Validators.required),
    available_days_times: new FormControl([])
  });

  availableDaysTimesOptionsModel: number[];
  availableDaysTimesOptions: IMultiSelectOption[];

  // Settings configuration
  mySettings: IMultiSelectSettings = {
    enableSearch: true,
    checkedStyle: 'fontawesome',
    buttonClasses: 'btn btn-default btn-block',
    dynamicTitleMaxItems: 3,
    displayAllSelectedText: true
  };

  constructor(private http: Http,
              private _router: Router) { }

  ngOnInit() {
    this.availableDaysTimesOptions = [
      { name: "Segunda - Manhã", id: "seg-manha"},
      { name: "Segunda - Tarde", id: "seg-tarde"},
      { name: "Segunda - Noite", id: "seg-noite"},
      { name: "Terça - Manhã", id: "ter-manha"},
      { name: "Terça - Tarde", id: "ter-tarde"},
      { name: "Terça - Noite", id: "ter-noite"},
      { name: "Quarta-feira - Manhã", id: "qua-manha"},
      { name: "Quarta-feira - Tarde", id: "qua-tarde"},
      { name: "Quarta-feira - Noite", id: "qua-noite"},
      { name: "Quinta-feira - Manhã", id: "qui-manha"},
      { name: "Quinta-feira - Tarde", id: "qui-tarde"},
      { name: "Quinta-feira - Noite", id: "qui-noite"},
      { name: "Sexta-feira - Manhã", id: "sex-manha"},
      { name: "Sexta-feira - Tarde", id: "sex-tarde"},
      { name: "Sexta-feira - Noite", id: "sex-noite"},
      { name: "Sábado - Manhã", id: "sab-manha"},
      { name: "Sábado - Tarde", id: "sab-tarde"},
      { name: "Sábado - Noite", id: "sab-noite"},
      { name: "Domingo - Manhã", id: "dom-manha"},
      { name: "Domingo - Tarde", id: "dom-tarde"},
      { name: "Domingo - Noite", id: "dom-noite"}
    ];
  }

  onFormSubmit(): void {
    this.formSubmitted = true;
    this.registerForm.controls['available_days_times'].setValue([]);  
    let formObj = this.registerForm.getRawValue();
    let serializedForm = JSON.stringify(formObj);

    window.scrollTo(0,0);
    console.log(formObj);


    if(this.registerForm.valid){
      this.http.post(this.registerPartnerUrl, serializedForm)
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

  onBack(): void {
    this._router.navigate(['home']);
  }
}
