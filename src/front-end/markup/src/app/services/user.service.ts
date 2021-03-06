import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { User } from "../models/user";

@Injectable()
export class UserService {
  constructor(private http: HttpClient) {
  }
  loadUser() {
    console.log('get user by id');
    return this.http.get<User>('http://localhost:8000/api/users/detail/');
  }

  register(user: User) {
    return this.http.post(`http://localhost:8000/api/auth/registration/`, user);
  }

  changeSettings(user: User) {
    return this.http.put(`http://localhost:8000/api/users/detail/`, user);
  }

  changeAvatar(file: FormData) {
    return this.http.put(`http://localhost:8000/api/users/detail/`, file);
  }

  loadUserList() {
    return this.http.get<User[]>('http://localhost:8000/api/users/');
  }
}
