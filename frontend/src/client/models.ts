export type AuthoritiesPublic = {
	data: Array<AuthorityPublic>;
	count: number;
};



export type AuthorityCreate = {
	name: string;
};



export type AuthorityPublic = {
	name: string;
	id: number;
	owner_id: number;
};



export type AuthorityUpdate = {
	name?: string | null;
};



export type Body_login_login_access_token = {
	grant_type?: string | null;
	username: string;
	password: string;
	scope?: string;
	client_id?: string | null;
	client_secret?: string | null;
};



export type Circs_GroupCreate = {
	group: string;
	desc: string;
};



export type Circs_GroupPublic = {
	group: string;
	desc: string;
	id: number;
	owner_id: number;
};



export type Circs_GroupUpdate = {
	group?: string | null;
	desc?: string | null;
};



export type Circs_GroupsPublic = {
	data: Array<Circs_GroupPublic>;
	count: number;
};



export type ClaimCreate = {
	client_firstname: string;
	client_lastname: string;
	authority_id: number;
};



export type ClaimPublic = {
	client_firstname: string;
	client_lastname: string;
	authority_id: number;
	id: number;
};



export type ClaimUpdate = {
	client_firstname?: string | null;
	client_lastname?: string | null;
	authority_id: number;
};



export type ClaimsPublic = {
	data: Array<ClaimPublic>;
	count: number;
};



export type HTTPValidationError = {
	detail?: Array<ValidationError>;
};



export type ItemCreate = {
	title: string;
	description?: string | null;
};



export type ItemPublic = {
	title: string;
	description?: string | null;
	id: number;
	owner_id: number;
};



export type ItemUpdate = {
	title?: string | null;
	description?: string | null;
};



export type ItemsPublic = {
	data: Array<ItemPublic>;
	count: number;
};



export type Message = {
	message: string;
};



export type NewPassword = {
	token: string;
	new_password: string;
};



export type ReferralCreate = {
	source_id: number;
	claim_id: number;
};



export type ReferralPublic = {
	source_id: number;
	claim_id: number;
	id: number;
	owner_id: number;
};



export type ReferralUpdate = {
	source_id?: number | null;
	claim_id: number;
};



export type Referral_AllocationCreate = {
	Source: string;
};



export type Referral_AllocationPublic = {
	Source: string;
	id: number;
	owner_id: number;
};



export type Referral_AllocationUpdate = {
	Source?: string | null;
};



export type Referral_AllocationsPublic = {
	data: Array<Referral_AllocationPublic>;
	count: number;
};



export type ReferralsPublic = {
	data: Array<ReferralPublic>;
	count: number;
};



export type RequestCreate = {
	type: string;
	source_id: number;
	client_firstname: string;
	client_lastname: string;
	authority_id: number;
};



export type SourceCreate = {
	source_name: string;
};



export type SourcePublic = {
	source_name: string;
	id: number;
	owner_id: number;
};



export type SourceUpdate = {
	source_name?: string | null;
};



export type Source_RateCreate = {
	rate: number;
};



export type Source_RatePublic = {
	rate: number;
	id: number;
	owner_id: number;
};



export type Source_RateUpdate = {
	rate?: number | null;
};



export type Source_RatesPublic = {
	data: Array<Source_RatePublic>;
	count: number;
};



export type SourcesPublic = {
	data: Array<SourcePublic>;
	count: number;
};



export type SupplierCreate = {
	name: string;
};



export type SupplierPublic = {
	name: string;
	id: number;
	owner_id: number;
};



export type SupplierUpdate = {
	name?: string | null;
};



export type Supplier_RateCreate = {
	rate: number;
};



export type Supplier_RatePublic = {
	rate: number;
	id: number;
	owner_id: number;
};



export type Supplier_RateUpdate = {
	rate?: number | null;
};



export type Supplier_RatesPublic = {
	data: Array<Supplier_RatePublic>;
	count: number;
};



export type SuppliersPublic = {
	data: Array<SupplierPublic>;
	count: number;
};



export type Token = {
	access_token: string;
	token_type?: string;
};



export type UpdatePassword = {
	current_password: string;
	new_password: string;
};



export type UserCreate = {
	email: string;
	is_active?: boolean;
	is_superuser?: boolean;
	full_name?: string | null;
	password: string;
};



export type UserPublic = {
	email: string;
	is_active?: boolean;
	is_superuser?: boolean;
	full_name?: string | null;
	id: number;
};



export type UserRegister = {
	email: string;
	password: string;
	full_name?: string | null;
};



export type UserUpdate = {
	email?: string | null;
	is_active?: boolean;
	is_superuser?: boolean;
	full_name?: string | null;
	password?: string | null;
};



export type UserUpdateMe = {
	full_name?: string | null;
	email?: string | null;
};



export type UsersPublic = {
	data: Array<UserPublic>;
	count: number;
};



export type ValidationError = {
	loc: Array<string | number>;
	msg: string;
	type: string;
};



export type Veh_GroupCreate = {
	group: string;
	desc: string;
};



export type Veh_GroupPublic = {
	group: string;
	desc: string;
	id: number;
	owner_id: number;
};



export type Veh_GroupUpdate = {
	group?: string | null;
	desc?: string | null;
};



export type Veh_GroupsPublic = {
	data: Array<Veh_GroupPublic>;
	count: number;
};

