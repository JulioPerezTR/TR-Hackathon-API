import { HttpClient, HttpResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { ResponseData } from './../models/responseData.model';

@Injectable({
	providedIn: 'root'
})
export class GeneralService {
	constructor(private http: HttpClient) { }

	getCardsData(): Observable<any> {
    return this.http.get<Array<ResponseData>>(
      `http://127.0.0.1:5000/get_main_data?operation_type`
    );
	}
}
