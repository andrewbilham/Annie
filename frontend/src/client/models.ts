export type AuthoritiesPublic = {
	data: Array<AuthorityPublic>;
	count: number;
};



export type AuthorityCreate = {
	name?: string | null;
};



export type AuthorityPublic = {
	name?: string | null;
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
	client_address_1?: string | null;
	client_address_town?: string | null;
	client_address_postcode?: string | null;
	client_vehicle_reg?: string | null;
	client_insurer?: string | null;
	client_insurer_policyno?: string | null;
	client_phone?: string | null;
	client_mobile?: string | null;
	client_email?: string | null;
	authority_id?: number | null;
	plate_type?: string | null;
	accident_date?: string | null;
	accident_time?: string | null;
	accident_location?: string | null;
	accident_circs?: string | null;
	tp_firstname?: string | null;
	tp_lastname?: string | null;
	tp_address_1?: string | null;
	tp_address_town?: string | null;
	tp_address_postcode?: string | null;
	tp_vehicle_reg?: string | null;
	tp_insurer?: string | null;
	tp_insurer_polcyno?: string | null;
	tp_phone?: string | null;
	tp_mobile?: string | null;
};



export type ClaimPublic = {
	client_firstname: string;
	client_lastname: string;
	client_address_1?: string | null;
	client_address_town?: string | null;
	client_address_postcode?: string | null;
	client_vehicle_reg?: string | null;
	client_insurer?: string | null;
	client_insurer_policyno?: string | null;
	client_phone?: string | null;
	client_mobile?: string | null;
	client_email?: string | null;
	authority_id?: number | null;
	plate_type?: string | null;
	accident_date?: string | null;
	accident_time?: string | null;
	accident_location?: string | null;
	accident_circs?: string | null;
	tp_firstname?: string | null;
	tp_lastname?: string | null;
	tp_address_1?: string | null;
	tp_address_town?: string | null;
	tp_address_postcode?: string | null;
	tp_vehicle_reg?: string | null;
	tp_insurer?: string | null;
	tp_insurer_polcyno?: string | null;
	tp_phone?: string | null;
	tp_mobile?: string | null;
	id: number;
};



export type ClaimUpdate = {
	client_firstname?: string | null;
	client_lastname?: string | null;
	client_address_1?: string | null;
	client_address_town?: string | null;
	client_address_postcode?: string | null;
	client_vehicle_reg?: string | null;
	client_insurer?: string | null;
	client_insurer_policyno?: string | null;
	client_phone?: string | null;
	client_mobile?: string | null;
	client_email?: string | null;
	authority_id?: number | null;
	plate_type?: string | null;
	accident_date?: string | null;
	accident_time?: string | null;
	accident_location?: string | null;
	accident_circs?: string | null;
	tp_firstname?: string | null;
	tp_lastname?: string | null;
	tp_address_1?: string | null;
	tp_address_town?: string | null;
	tp_address_postcode?: string | null;
	tp_vehicle_reg?: string | null;
	tp_insurer?: string | null;
	tp_insurer_polcyno?: string | null;
	tp_phone?: string | null;
	tp_mobile?: string | null;
};



export type ClaimsPublic = {
	data: Array<ClaimPublic>;
	count: number;
};



export type HTTPValidationError = {
  detail?: Array<ValidationError>
}

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
	source_id?: number | null;
	claim_id?: number | null;
	supplier_id?: number | null;
	type?: string | null;
	authority_id?: number | null;
};



export type ReferralPublic = {
	source_id?: number | null;
	claim_id?: number | null;
	supplier_id?: number | null;
	type?: string | null;
	authority_id?: number | null;
	id: number;
	source: Source;
};



export type ReferralUpdate = {
	source_id?: number | null;
	claim_id?: number | null;
	supplier_id?: number | null;
	type?: string | null;
	authority_id?: number | null;
	daystohire?: number | null;
	creditrepair?: string | null;
};



export type Referral_AllocationCreate = {
	supplier_id: number;
	referral_id: number;
	sentdate: string;
	status: string;
	responsedate?: string | null;
};



export type Referral_AllocationPublic = {
	supplier_id?: number | null;
	referral_id?: number | null;
	sentdate?: string | null;
	status?: string | null;
	responsedate?: string | null;
	id: number;
	owner_id: number;
};



export type Referral_AllocationUpdate = {
	supplier_id?: number | null;
	referral_id?: number | null;
	sentdate?: string | null;
	status?: string | null;
	responsedate?: string | null;
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
	source_id: number;
	type?: string | null;
	daystohire?: number | null;
	creditrepair?: string | null;
	authority_id?: number | null;
	client_firstname: string;
	client_lastname: string;
	client_address_1?: string | null;
	client_address_town?: string | null;
	client_address_postcode?: string | null;
	client_vehicle_reg?: string | null;
	client_insurer?: string | null;
	client_insurer_policyno?: string | null;
	client_phone?: string | null;
	client_mobile?: string | null;
	client_email?: string | null;
	plate_type?: string | null;
	accident_date?: string | null;
	accident_time?: string | null;
	accident_location?: string | null;
	accident_circs?: string | null;
	tp_firstname?: string | null;
	tp_lastname?: string | null;
	tp_address_1?: string | null;
	tp_address_town?: string | null;
	tp_address_postcode?: string | null;
	tp_vehicle_reg?: string | null;
	tp_insurer?: string | null;
	tp_insurer_polcyno?: string | null;
	tp_phone?: string | null;
	tp_mobile?: string | null;
	circs_grade_id?: number | null;
	veh_group_id?: number | null;
	circs_group_id?: number | null;
};



export type Source = {
	created_datetime?: string | null;
	updated_datetime?: string | null;
	source_name: string;
	id?: number | null;
	owner_id?: number | null;
};



export type SourceCreate = {
	source_name: string;
};



export type SourcePublic = {
	source_name: string;
	id: number;
};



export type SourceUpdate = {
	source_name?: string | null;
};



export type Source_RateCreate = {
	authority_id?: number | null;
	plate_type?: string | null;
	veh_group_id?: number | null;
	circs_group_id?: number | null;
	type?: string | null;
	rate?: number | null;
	hire_length?: number | null;
	source_id?: number | null;
};



export type Source_RatePublic = {
	authority_id?: number | null;
	plate_type?: string | null;
	veh_group_id?: number | null;
	circs_group_id?: number | null;
	type?: string | null;
	rate?: number | null;
	hire_length?: number | null;
	source_id?: number | null;
};



export type Source_RateUpdate = {
	authority_id?: number | null;
	plate_type?: string | null;
	veh_group_id?: number | null;
	circs_group_id?: number | null;
	type?: string | null;
	rate?: number | null;
	hire_length?: number | null;
	source_id?: number | null;
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
	address_1?: string | null;
	address_town?: string | null;
	address_postcode?: string | null;
	base_rate: number;
	Email?: string | null;
	Tel?: number | null;
};



export type SupplierPublic = {
	name: string;
	address_1?: string | null;
	address_town?: string | null;
	address_postcode?: string | null;
	base_rate: number;
	Email?: string | null;
	Tel?: number | null;
	id: number;
};



export type SupplierUpdate = {
	name?: string | null;
	address_1?: string | null;
	address_town?: string | null;
	address_postcode?: string | null;
	base_rate?: number | null;
	Email?: string | null;
	Tel?: number | null;
};



export type Supplier_RateCreate = {
	authority_id?: number | null;
	plate_type?: string | null;
	veh_group_id?: number | null;
	circs_group_id?: number | null;
	type?: string | null;
	rate?: number | null;
	hire_length?: number | null;
	supplier_id?: number | null;
};



export type Supplier_RatePublic = {
	authority_id?: number | null;
	plate_type?: string | null;
	veh_group_id?: number | null;
	circs_group_id?: number | null;
	type?: string | null;
	rate?: number | null;
	hire_length?: number | null;
	supplier_id?: number | null;
	id: number;
	owner_id: number;
};



export type Supplier_RateUpdate = {
	authority_id?: number | null;
	plate_type?: string | null;
	veh_group_id?: number | null;
	circs_group_id?: number | null;
	type?: string | null;
	rate?: number | null;
	hire_length?: number | null;
	supplier_id?: number | null;
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
	group?: string | null;
	desc?: string | null;
};



export type Veh_GroupPublic = {
	group?: string | null;
	desc?: string | null;
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

