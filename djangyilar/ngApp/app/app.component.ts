import { Component } from '@angular/core';
import { ROUTER_DIRECTIVES } from '@angular/router';

// import { ContactUsComponent } form './contactus.component';

@Component({
    selector: 'my-app',
    template: `
        <nav>
          <a href="/contact/">Contact Us</a>
          <a routerLink="/portfolio" routerLinkActive="active">Portfolio</a>
          <a routerLink="/aboutme" routerLinkActive="active">About Mee</a>
        </nav>
        <router-outlet></router-outlet>
    `,
    directives: [ROUTER_DIRECTIVES]
})
export class AppComponent { }

//<a routerLink="/djcomponent" routerLinkActive="active">Dj+ngComp</a>
