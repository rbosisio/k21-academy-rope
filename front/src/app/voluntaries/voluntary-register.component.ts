import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators  } from '@angular/forms'
import { Http } from '@angular/http';
import { Router, ActivatedRoute } from "@angular/router";
import { IMultiSelectOption, IMultiSelectSettings, IMultiSelectTexts } from 'angular-2-dropdown-multiselect';

@Component({
  selector: 'app-voluntary-register',
  templateUrl: './voluntary-register.component.html',
  styleUrls: ['./voluntary-register.component.scss']
})
export class VoluntaryRegisterComponent implements OnInit {

  registerVoluntaryUrl: string = "http://admin.institutorope.com.br/api/volunteers/";

  fieldsRequiredMessage: string = "Preecha todos os campos obrigatórios.";
  errorMessage: string = "Ocorreu um erro no seu cadastro. Por favor tente novamente ou entre em contanto conosco.";
  successMessage: string = "Seu cadastrado como voluntário foi realizado com sucesso! Entraremos em contato em breve!";

  success: boolean = false;
  failed: boolean = false;
  formSubmitted: boolean = false;
  registerForm:FormGroup = new FormGroup({
    name: new FormControl('', Validators.required),
    nickname: new FormControl('', Validators.required),
    birthdate: new FormControl('', Validators.required),
    telephone: new FormControl('', Validators.required),
    cellphone: new FormControl('', Validators.required),
    email: new FormControl('', Validators.required),
    address: new FormControl('', Validators.required),
    personal_characteristics: new FormControl('', Validators.required),
    talents: new FormControl('', Validators.required),
    available_days_times: new FormControl([], Validators.required)
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
              private _route: ActivatedRoute,
              private _router: Router) { }

  ngOnInit(): void {
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
    let formObj = this.registerForm.getRawValue();
    let serializedForm = JSON.stringify(formObj);

    window.scrollTo(0,0);

    if(this.registerForm.valid){
      this.http.post(this.registerVoluntaryUrl, serializedForm)
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
