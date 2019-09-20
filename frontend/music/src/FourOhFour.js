import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class FourOhFour extends Component {
    render() {
        return (
            <div className="main-container">
                <p className="login">Username and password is required to enter this site. Please try again. 
                <br/>
                <Link className="try-again" to="/">Try again</Link> </p>
            </div>
        );
    }
}

export default FourOhFour;