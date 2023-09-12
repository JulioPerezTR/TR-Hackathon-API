import { HttpClient, HttpResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ResponseData } from './../models/responseData.model';

@Injectable({
	providedIn: 'root'
})
export class GeneralService {
	constructor(private http: HttpClient) { }

	getCardsData(type: string = ''): Observable<any> {
    return this.http.get<Array<ResponseData>>(
      `assets/CardsData${type}.json`
    );
	}
}
