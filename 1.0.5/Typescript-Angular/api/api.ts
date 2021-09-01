export * from './authentication.service';
import { AuthenticationService } from './authentication.service';
export * from './filteredAPI.service';
import { FilteredAPIService } from './filteredAPI.service';
export * from './genericAPI.service';
import { GenericAPIService } from './genericAPI.service';
export const APIS = [AuthenticationService, FilteredAPIService, GenericAPIService];
