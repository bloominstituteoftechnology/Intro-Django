import React, { Component } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

class MusicList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            music: [],
        }
    }
    componentDidMount() {
        let promise = axios.get(`http://localhost:8000/api/music/`);
        promise.then((response) => {
            console.log("CDM music", response);
            this.setState({
                response
            });
            })
            .catch((error) => {
                console.error(error);
            })
    }
    render() {
        console.log(this.state.music);
        return(
            <div>I'm a musiclist</div>
        )
        // return (
        //     <div>
        //         <div className="main-note-container">
        //             {this.state.music.map(music => {
        //                 return (
        //                     <div key={music.id} className="note-indiv">
        //                         <h1>{music.title}</h1>   
        //                         <h3>{music.composer_first_name}</h3>
        //                         <h3>{music.composer_last_name}</h3>
        //                     </div>              )
        //             })}
        //         </div>
        //     </div>
        // );
    }
    }
    
    export default MusicList;




