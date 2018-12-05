import React, { Component } from 'react'
import styled from 'styled-components'
import axios from 'axios'
import logo from './logo.svg'
import Login from './components/Login'
import Home from './components/Home'
class App extends Component {
  state = {
    isLoggedIn: false
  }

  componentDidMount() {
    const token = localStorage.getItem('token')
    if (token) { this.setState({ isLoggedIn: true }) }
  }

  login = (username, password) => {
    axios.post('http://127.0.0.1:8000/api-token-auth/', { username, password })
      .then(resp => {
        localStorage.setItem('token', resp.data.token)
        this.setState({ isLoggedIn: true })
      })
      .catch(function (error) {
        console.log(error);
      });
  }

  logout = (e) => {
    e.preventDefault()
    localStorage.clear()
    this.setState({ isLoggedIn: false })
  }

  render() {
    return (
      <Div1>
        <Img1 src={logo} alt="logo" />
        {
          this.state.isLoggedIn ? (<Home logout={this.logout} />) : (<Login login={this.login} />)
        }
      </Div1>
    )
  }
}

const Div1 = styled.div`
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
`

const Img1 = styled.img`
  animation: App-logo-spin1 infinite 30s linear;
  height: 20vmin;

  @keyframes App-logo-spin1 {
  from {
    transform: rotate(360deg);
  }
  to {
    transform: rotate(0deg);
  }
}
`

export default App;
