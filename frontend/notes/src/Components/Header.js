import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import '../index.css';

class Header extends Component {
  render() {
    return (
      <div className="main-container">
        <header className="header">
          <h1 className="title">Lambda-Django Notes</h1>
        </header>
        <p className="intro">
          To get started, enter <Link className="header-link" to='/notes'>here</Link>
        </p>
      </div>
    );
  }
}

export default Header;
