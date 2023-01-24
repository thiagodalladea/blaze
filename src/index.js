import React from 'react';
import ReactDOM from 'react-dom';
import { Routes,Route,BrowserRouter } from'react-router-dom';
import { WelcomePage } from'./WelcomePage.js';
import { DashboardPage } from './DashboardPage.js';

ReactDOM.render(
  <BrowserRouter>
      <Routes>
          <Route exact path='/' element={ <WelcomePage /> }/>
          <Route exact path='/dashboard' element={ <DashboardPage /> }/> 
      </Routes>
  </BrowserRouter>
, document.getElementById('root'))