import { Component, OnInit } from '@angular/core';
import { Http } from '@angular/http';
import { Dream } from "./dream";

@Component({
  selector: 'app-dream-list',
  templateUrl: './dream-list.component.html',
  styleUrls: ['./dream-list.component.scss']
})
export class DreamListComponent implements OnInit {

  dreamsListUrl: string = "http://admin.institutorope.com.br/api/dreams/status/aprovado/";
  dreams: Dream[] = [];

  constructor(private http: Http) { }

  ngOnInit() {
    this.http.get(this.dreamsListUrl).subscribe(data => {
      let results = JSON.parse(data['_body']);
      
      for(let result of results){

        let needs_splited = result.fields.dream_needs.split(';');
        if(needs_splited.slice(-1)[0] == "")
          needs_splited.pop();
        
        result.fields.dream_needs = needs_splited;

        this.dreams.push(result.fields);
      }

      console.log(this.dreams);
    }); 
  }

  // handleClick():void {
  // 	console.log('aqui');
  // }

}
