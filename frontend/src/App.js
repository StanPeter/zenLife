import React, { Component } from 'react';
import { Link, Route } from 'react-router-dom';
import Users from './containers/Users';
import asyncComponent from './hoc/asyncComponent';
import axios from 'axios';

const AsyncPizza = asyncComponent(() => {
    return import('./containers/Pizza.js');
});

class App extends Component {
    componentDidMount() {
        axios.get('http://127.0.0.1:8081/api/posts/', { headers: { 'Content-Type': 'application/json' } }).then(res => console.log(res, 'res'));
    }

    render() {
        return (
            <div>
                <div>
                    <Link to="/">Users</Link> | <Link to="/pizza">Pizza</Link>
                </div>
                <div>
                    <Route path="/" exact component={Users} />
                    <Route path="/pizza" component={AsyncPizza} />
                </div>
            </div>
        );
    }
}

export default App;