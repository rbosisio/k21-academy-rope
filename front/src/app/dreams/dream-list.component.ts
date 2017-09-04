import { Component, OnInit } from '@angular/core';
import { Http } from '@angular/http';
import { Dream } from "./dream";

@Component({
  selector: 'app-dream-list',
  templateUrl: './dream-list.component.html',
  styleUrls: ['./dream-list.component.scss']
})
export class DreamListComponent implements OnInit {

  dreamsListUrl: string = "http://sonhos.institutorope.com.br:8000/api/dreams/status/aprovado/";
  dreams: Dream[] = [];

  constructor(private http: Http) { }

  ngOnInit() {
    this.http.get(this.dreamsListUrl).subscribe(data => {
      let results = JSON.parse(data['_body']);
      
      for(let result of results){
        this.dreams.push(result.fields);
      }

      console.log(this.dreams);
    }); 
  }

}
