import React from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';
import {defaultTheme, GlobalStyle} from './styles';
import {Provider} from 'react-redux';
import {ThemeProvider} from 'styled-components';
import store from './store';
import Home from './pages/Home';
import Login from './pages/Login';
import EmailSignUp from './pages/Login/SingUp/EmailForm';
import CongratsMessage from './pages/Login/SingUp/CongratsDiv';
import VerificationForm from './pages/Login/SingUp/Verification'
import TournamentOverview from './pages/TournamentOverview';
import TournamentAdmin from './pages/TournamentAdmin.jsx';
import CreateTournament from './pages/CreateTournament';
import Message from './pages/CreateTournament/message';
import PrivateOrPublic from './pages/CreateTournament/PrivateOr';
import DetailsCreate from './pages/CreateTournament/DetailsTournament';
import AboutUs from "./pages/AboutUs"
// import BracketPage from './pages/BracketPage';
import Bracket from './pages/Bracket';
import {PageContainer, PageContent} from './styles/page-layout';
import Profile from "./pages/Profile/index";
import Standing from "./pages/Standing";
import EditProfile from "./pages/Profile/EditProfile";
import Tournaments from "./pages/Tournaments";
import LoginInUserSideMenu from "./components/LoginUserMenu"


ReactDOM.render(
  <Provider store={ store }>
    <ThemeProvider theme={defaultTheme}>
      <GlobalStyle />
      <Router>
      <PageContainer>
            <PageContent>
            <Switch>
              <Route exact path="/" component={ Home } />
              <Route exact path="/tournament/:id" component={TournamentOverview} />
              <Route exact path="/tournament/:id/admin" component={TournamentAdmin} />
              <Route exact path="/tournaments" component={Tournaments} />
              <Route exact path="/tournament/:id/bracket" component={Bracket} />
              <Route exact path="/tournament/:id/standing" component={Standing} />
              <Route exact path="/login" component={ Login } />
              <Route exact path="/registration" component={ EmailSignUp } />
              <Route exact path="/confirmation" component={ CongratsMessage } />
              <Route exact path="/verification" component={ VerificationForm} />
              <Route exact path="/create" component={ CreateTournament } />
              <Route exact path="/message" component={ Message } />
              <Route exact path="/privacy" component={ PrivateOrPublic } />
              <Route exact path="/details" component={ DetailsCreate } />
              <Route exact path="/user/profile" component={Profile} />
              <Route exact path="/user/profile/edit" component={EditProfile} />
              <Route exact path="/menu" component={ LoginInUserSideMenu } />
              <Route exact path="/aboutus" component={ AboutUs } />

            </Switch>
            </PageContent>
        </PageContainer>
    </Router>
    </ThemeProvider>
  </Provider>,

    document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals

