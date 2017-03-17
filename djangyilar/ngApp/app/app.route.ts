import { provideRouter, RouterConfig } from '@angular/router';
import { ContactUsComponent } from "./contactus.component";
import { PortfolioComponent } from "./portfolio.component";
import { ComingSoonComponent } from "./comingsoon.component";
import { AboutMeComponent } from "./aboutme.component";
import { DjangoComponent } from "./django.component";


const routes: RouterConfig = [
  { path: '',redirectTo: '/portfolio',pathMatch: 'full' },
  { path: 'contactus', component: ContactUsComponent },
  { path: 'aboutme', component: AboutMeComponent },
  { path: 'comingsoon', component: ComingSoonComponent },
  { path: 'portfolio', component: PortfolioComponent },
  { path: 'djcomponent', component: DjangoComponent },
];

export const appRouterProviders = [
  provideRouter(routes)
];
