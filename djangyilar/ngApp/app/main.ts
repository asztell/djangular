import { bootstrap }    from '@angular/platform-browser-dynamic';
import { HTTP_PROVIDERS } from "@angular/http";
import { enableProdMode } from '@angular/core';

import { AppComponent } from './app.component';
import { appRouterProviders } from "./app.route";


enableProdMode();
bootstrap(AppComponent, [
  appRouterProviders,
  HTTP_PROVIDERS
])
.catch(err => console.error(err));