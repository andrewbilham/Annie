import type { CancelablePromise } from './core/CancelablePromise';
import { OpenAPI } from './core/OpenAPI';
import { request as __request } from './core/request';

import type { Body_login_login_access_token,Message,NewPassword,Token,UserPublic,UpdatePassword,UserCreate,UserRegister,UsersPublic,UserUpdate,UserUpdateMe,ItemCreate,ItemPublic,ItemsPublic,ItemUpdate,SourceCreate,SourcePublic,SourcesPublic,SourceUpdate,SupplierCreate,SupplierPublic,SuppliersPublic,SupplierUpdate,Circs_GroupCreate,Circs_GroupPublic,Circs_GroupsPublic,Circs_GroupUpdate,ClaimCreate,ClaimPublic,ClaimsPublic,ClaimUpdate,Referral_AllocationCreate,Referral_AllocationPublic,Referral_AllocationsPublic,Referral_AllocationUpdate,ReferralCreate,ReferralPublic,ReferralsPublic,ReferralUpdate,Source_RateCreate,Source_RatePublic,Source_RatesPublic,Source_RateUpdate,Supplier_RateCreate,Supplier_RatePublic,Supplier_RatesPublic,Supplier_RateUpdate,Veh_GroupCreate,Veh_GroupPublic,Veh_GroupsPublic,Veh_GroupUpdate,AuthoritiesPublic,AuthorityCreate,AuthorityPublic,AuthorityUpdate,RequestCreate } from './models';

export type TDataLoginAccessToken = {
                formData: Body_login_login_access_token
                
            }
export type TDataRecoverPassword = {
                email: string
                
            }
export type TDataResetPassword = {
                requestBody: NewPassword
                
            }
export type TDataRecoverPasswordHtmlContent = {
                email: string
                
            }

export class LoginService {

	/**
	 * Login Access Token
	 * OAuth2 compatible token login, get an access token for future requests
	 * @returns Token Successful Response
	 * @throws ApiError
	 */
	public static loginAccessToken(data: TDataLoginAccessToken): CancelablePromise<Token> {
		const {
formData,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/login/access-token',
			formData: formData,
			mediaType: 'application/x-www-form-urlencoded',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Test Token
	 * Test access token
	 * @returns UserPublic Successful Response
	 * @throws ApiError
	 */
	public static testToken(): CancelablePromise<UserPublic> {
				return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/login/test-token',
		});
	}

	/**
	 * Recover Password
	 * Password Recovery
	 * @returns Message Successful Response
	 * @throws ApiError
	 */
	public static recoverPassword(data: TDataRecoverPassword): CancelablePromise<Message> {
		const {
email,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/password-recovery/{email}',
			path: {
				email
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Reset Password
	 * Reset password
	 * @returns Message Successful Response
	 * @throws ApiError
	 */
	public static resetPassword(data: TDataResetPassword): CancelablePromise<Message> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/reset-password/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Recover Password Html Content
	 * HTML Content for Password Recovery
	 * @returns string Successful Response
	 * @throws ApiError
	 */
	public static recoverPasswordHtmlContent(data: TDataRecoverPasswordHtmlContent): CancelablePromise<string> {
		const {
email,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/password-recovery-html-content/{email}',
			path: {
				email
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataReadUsers = {
                limit?: number
skip?: number
                
            }
export type TDataCreateUser = {
                requestBody: UserCreate
                
            }
export type TDataUpdateUserMe = {
                requestBody: UserUpdateMe
                
            }
export type TDataUpdatePasswordMe = {
                requestBody: UpdatePassword
                
            }
export type TDataRegisterUser = {
                requestBody: UserRegister
                
            }
export type TDataReadUserById = {
                userId: number
                
            }
export type TDataUpdateUser = {
                requestBody: UserUpdate
userId: number
                
            }
export type TDataDeleteUser = {
                userId: number
                
            }

export class UsersService {

	/**
	 * Read Users
	 * Retrieve users.
	 * @returns UsersPublic Successful Response
	 * @throws ApiError
	 */
	public static readUsers(data: TDataReadUsers = {}): CancelablePromise<UsersPublic> {
		const {
limit = 100,
skip = 0,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/users/',
			query: {
				skip, limit
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create User
	 * Create new user.
	 * @returns UserPublic Successful Response
	 * @throws ApiError
	 */
	public static createUser(data: TDataCreateUser): CancelablePromise<UserPublic> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/users/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read User Me
	 * Get current user.
	 * @returns UserPublic Successful Response
	 * @throws ApiError
	 */
	public static readUserMe(): CancelablePromise<UserPublic> {
				return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/users/me',
		});
	}

	/**
	 * Delete User Me
	 * Delete own user.
	 * @returns Message Successful Response
	 * @throws ApiError
	 */
	public static deleteUserMe(): CancelablePromise<Message> {
				return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/users/me',
		});
	}

	/**
	 * Update User Me
	 * Update own user.
	 * @returns UserPublic Successful Response
	 * @throws ApiError
	 */
	public static updateUserMe(data: TDataUpdateUserMe): CancelablePromise<UserPublic> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'PATCH',
			url: '/api/v1/users/me',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Update Password Me
	 * Update own password.
	 * @returns Message Successful Response
	 * @throws ApiError
	 */
	public static updatePasswordMe(data: TDataUpdatePasswordMe): CancelablePromise<Message> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'PATCH',
			url: '/api/v1/users/me/password',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Register User
	 * Create new user without the need to be logged in.
	 * @returns UserPublic Successful Response
	 * @throws ApiError
	 */
	public static registerUser(data: TDataRegisterUser): CancelablePromise<UserPublic> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/users/signup',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read User By Id
	 * Get a specific user by id.
	 * @returns UserPublic Successful Response
	 * @throws ApiError
	 */
	public static readUserById(data: TDataReadUserById): CancelablePromise<UserPublic> {
		const {
userId,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/users/{user_id}',
			path: {
				user_id: userId
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Update User
	 * Update a user.
	 * @returns UserPublic Successful Response
	 * @throws ApiError
	 */
	public static updateUser(data: TDataUpdateUser): CancelablePromise<UserPublic> {
		const {
requestBody,
userId,
} = data;
		return __request(OpenAPI, {
			method: 'PATCH',
			url: '/api/v1/users/{user_id}',
			path: {
				user_id: userId
			},
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete User
	 * Delete a user.
	 * @returns Message Successful Response
	 * @throws ApiError
	 */
	public static deleteUser(data: TDataDeleteUser): CancelablePromise<Message> {
		const {
userId,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/users/{user_id}',
			path: {
				user_id: userId
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataTestEmail = {
                emailTo: string
                
            }

export class UtilsService {

	/**
	 * Test Email
	 * Test emails.
	 * @returns Message Successful Response
	 * @throws ApiError
	 */
	public static testEmail(data: TDataTestEmail): CancelablePromise<Message> {
		const {
emailTo,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/utils/test-email/',
			query: {
				email_to: emailTo
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataReadItems = {
                limit?: number
skip?: number
                
            }
export type TDataCreateItem = {
                requestBody: ItemCreate
                
            }
export type TDataReadItem = {
                id: number
                
            }
export type TDataUpdateItem = {
                id: number
requestBody: ItemUpdate
                
            }
export type TDataDeleteItem = {
                id: number
                
            }

export class ItemsService {

	/**
	 * Read Items
	 * Retrieve items.
	 * @returns ItemsPublic Successful Response
	 * @throws ApiError
	 */
	public static readItems(data: TDataReadItems = {}): CancelablePromise<ItemsPublic> {
		const {
limit = 100,
skip = 0,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/items/',
			query: {
				skip, limit
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Item
	 * Create new item.
	 * @returns ItemPublic Successful Response
	 * @throws ApiError
	 */
	public static createItem(data: TDataCreateItem): CancelablePromise<ItemPublic> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/items/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read Item
	 * Get item by ID.
	 * @returns ItemPublic Successful Response
	 * @throws ApiError
	 */
	public static readItem(data: TDataReadItem): CancelablePromise<ItemPublic> {
		const {
id,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/items/{id}',
			path: {
				id
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Update Item
	 * Update an item.
	 * @returns ItemPublic Successful Response
	 * @throws ApiError
	 */
	public static updateItem(data: TDataUpdateItem): CancelablePromise<ItemPublic> {
		const {
id,
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'PUT',
			url: '/api/v1/items/{id}',
			path: {
				id
			},
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Item
	 * Delete an item.
	 * @returns Message Successful Response
	 * @throws ApiError
	 */
	public static deleteItem(data: TDataDeleteItem): CancelablePromise<Message> {
		const {
id,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/items/{id}',
			path: {
				id
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataReadSources = {
                limit?: number
skip?: number
                
            }
export type TDataCreateSource = {
                requestBody: SourceCreate
                
            }
export type TDataReadSource = {
                id: number
                
            }
export type TDataUpdateSource = {
                id: number
requestBody: SourceUpdate
                
            }
export type TDataDeleteSource = {
                id: number
                
            }

export class SourcesService {

	/**
	 * Read Sources
	 * Retrieve sources.
	 * @returns SourcesPublic Successful Response
	 * @throws ApiError
	 */
	public static readSources(data: TDataReadSources = {}): CancelablePromise<SourcesPublic> {
		const {
limit = 100,
skip = 0,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/sources/',
			query: {
				skip, limit
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Source
	 * Create new source.
	 * @returns SourcePublic Successful Response
	 * @throws ApiError
	 */
	public static createSource(data: TDataCreateSource): CancelablePromise<SourcePublic> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/sources/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read Source
	 * Get source by ID.
	 * @returns SourcePublic Successful Response
	 * @throws ApiError
	 */
	public static readSource(data: TDataReadSource): CancelablePromise<SourcePublic> {
		const {
id,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/sources/{id}',
			path: {
				id
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Update Source
	 * Update an source.
	 * @returns SourcePublic Successful Response
	 * @throws ApiError
	 */
	public static updateSource(data: TDataUpdateSource): CancelablePromise<SourcePublic> {
		const {
id,
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'PUT',
			url: '/api/v1/sources/{id}',
			path: {
				id
			},
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Source
	 * Delete an source.
	 * @returns Message Successful Response
	 * @throws ApiError
	 */
	public static deleteSource(data: TDataDeleteSource): CancelablePromise<Message> {
		const {
id,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/sources/{id}',
			path: {
				id
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataReadSuppliers = {
                limit?: number
skip?: number
                
            }
export type TDataCreateSupplier = {
                requestBody: SupplierCreate
                
            }
export type TDataReadSupplier = {
                id: number
                
            }
export type TDataUpdateSupplier = {
                id: number
requestBody: SupplierUpdate
                
            }
export type TDataDeleteSupplier = {
                id: number
                
            }

export class SuppliersService {

	/**
	 * Read Suppliers
	 * Retrieve suppliers.
	 * @returns SuppliersPublic Successful Response
	 * @throws ApiError
	 */
	public static readSuppliers(data: TDataReadSuppliers = {}): CancelablePromise<SuppliersPublic> {
		const {
limit = 100,
skip = 0,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/suppliers/',
			query: {
				skip, limit
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Supplier
	 * Create new supplier.
	 * @returns SupplierPublic Successful Response
	 * @throws ApiError
	 */
	public static createSupplier(data: TDataCreateSupplier): CancelablePromise<SupplierPublic> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/suppliers/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read Supplier
	 * Get supplier by ID.
	 * @returns SupplierPublic Successful Response
	 * @throws ApiError
	 */
	public static readSupplier(data: TDataReadSupplier): CancelablePromise<SupplierPublic> {
		const {
id,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/suppliers/{id}',
			path: {
				id
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Update Supplier
	 * Update an supplier.
	 * @returns SupplierPublic Successful Response
	 * @throws ApiError
	 */
	public static updateSupplier(data: TDataUpdateSupplier): CancelablePromise<SupplierPublic> {
		const {
id,
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'PUT',
			url: '/api/v1/suppliers/{id}',
			path: {
				id
			},
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Supplier
	 * Delete an supplier.
	 * @returns Message Successful Response
	 * @throws ApiError
	 */
	public static deleteSupplier(data: TDataDeleteSupplier): CancelablePromise<Message> {
		const {
id,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/suppliers/{id}',
			path: {
				id
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataReadCircsGroups = {
                limit?: number
skip?: number
                
            }
export type TDataCreateCircsGroup = {
                requestBody: Circs_GroupCreate
                
            }
export type TDataReadCircsGroup = {
                id: number
                
            }
export type TDataUpdateCircsGroup = {
                id: number
requestBody: Circs_GroupUpdate
                
            }
export type TDataDeleteCircsGroup = {
                id: number
                
            }

export class CircsGroupsService {

	/**
	 * Read Circs Groups
	 * Retrieve circs_groups.
	 * @returns Circs_GroupsPublic Successful Response
	 * @throws ApiError
	 */
	public static readCircsGroups(data: TDataReadCircsGroups = {}): CancelablePromise<Circs_GroupsPublic> {
		const {
limit = 100,
skip = 0,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/circs_groups/',
			query: {
				skip, limit
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Circs Group
	 * Create new circs_group.
	 * @returns Circs_GroupPublic Successful Response
	 * @throws ApiError
	 */
	public static createCircsGroup(data: TDataCreateCircsGroup): CancelablePromise<Circs_GroupPublic> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/circs_groups/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read Circs Group
	 * Get circs_group by ID.
	 * @returns Circs_GroupPublic Successful Response
	 * @throws ApiError
	 */
	public static readCircsGroup(data: TDataReadCircsGroup): CancelablePromise<Circs_GroupPublic> {
		const {
id,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/circs_groups/{id}',
			path: {
				id
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Update Circs Group
	 * Update an circs_group.
	 * @returns Circs_GroupPublic Successful Response
	 * @throws ApiError
	 */
	public static updateCircsGroup(data: TDataUpdateCircsGroup): CancelablePromise<Circs_GroupPublic> {
		const {
id,
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'PUT',
			url: '/api/v1/circs_groups/{id}',
			path: {
				id
			},
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Circs Group
	 * Delete an circs_group.
	 * @returns Message Successful Response
	 * @throws ApiError
	 */
	public static deleteCircsGroup(data: TDataDeleteCircsGroup): CancelablePromise<Message> {
		const {
id,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/circs_groups/{id}',
			path: {
				id
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataReadClaims = {
                limit?: number
skip?: number
                
            }
export type TDataCreateClaim = {
                requestBody: ClaimCreate
                
            }
export type TDataReadClaim = {
                id: number
                
            }
export type TDataUpdateClaim = {
                id: number
requestBody: ClaimUpdate
                
            }
export type TDataDeleteClaim = {
                id: number
                
            }

export class ClaimsService {

	/**
	 * Read Claims
	 * Retrieve claims.
	 * @returns ClaimsPublic Successful Response
	 * @throws ApiError
	 */
	public static readClaims(data: TDataReadClaims = {}): CancelablePromise<ClaimsPublic> {
		const {
limit = 100,
skip = 0,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/claims/',
			query: {
				skip, limit
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Claim
	 * Create new claim.
	 * @returns ClaimPublic Successful Response
	 * @throws ApiError
	 */
	public static createClaim(data: TDataCreateClaim): CancelablePromise<ClaimPublic> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/claims/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read Claim
	 * Get claim by ID.
	 * @returns ClaimPublic Successful Response
	 * @throws ApiError
	 */
	public static readClaim(data: TDataReadClaim): CancelablePromise<ClaimPublic> {
		const {
id,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/claims/{id}',
			path: {
				id
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Update Claim
	 * Update an claim.
	 * @returns ClaimPublic Successful Response
	 * @throws ApiError
	 */
	public static updateClaim(data: TDataUpdateClaim): CancelablePromise<ClaimPublic> {
		const {
id,
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'PUT',
			url: '/api/v1/claims/{id}',
			path: {
				id
			},
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Claim
	 * Delete an claim.
	 * @returns Message Successful Response
	 * @throws ApiError
	 */
	public static deleteClaim(data: TDataDeleteClaim): CancelablePromise<Message> {
		const {
id,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/claims/{id}',
			path: {
				id
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataReadReferralAllocations = {
                limit?: number
skip?: number
                
            }
export type TDataCreateReferralAllocation = {
                requestBody: Referral_AllocationCreate
                
            }
export type TDataReadReferralAllocation = {
                id: number
                
            }
export type TDataUpdateReferralAllocation = {
                id: number
requestBody: Referral_AllocationUpdate
                
            }
export type TDataDeleteReferralAllocation = {
                id: number
                
            }

export class ReferralsAllocationsService {

	/**
	 * Read Referral Allocations
	 * Retrieve referral_allocations.
	 * @returns Referral_AllocationsPublic Successful Response
	 * @throws ApiError
	 */
	public static readReferralAllocations(data: TDataReadReferralAllocations = {}): CancelablePromise<Referral_AllocationsPublic> {
		const {
limit = 100,
skip = 0,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/referrals_allocations/',
			query: {
				skip, limit
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Referral Allocation
	 * Create new referral_allocation.
	 * @returns Referral_AllocationPublic Successful Response
	 * @throws ApiError
	 */
	public static createReferralAllocation(data: TDataCreateReferralAllocation): CancelablePromise<Referral_AllocationPublic> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/referrals_allocations/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read Referral Allocation
	 * Get referral_allocation by ID.
	 * @returns Referral_AllocationPublic Successful Response
	 * @throws ApiError
	 */
	public static readReferralAllocation(data: TDataReadReferralAllocation): CancelablePromise<Referral_AllocationPublic> {
		const {
id,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/referrals_allocations/{id}',
			path: {
				id
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Update Referral Allocation
	 * Update an referral_allocation.
	 * @returns Referral_AllocationPublic Successful Response
	 * @throws ApiError
	 */
	public static updateReferralAllocation(data: TDataUpdateReferralAllocation): CancelablePromise<Referral_AllocationPublic> {
		const {
id,
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'PUT',
			url: '/api/v1/referrals_allocations/{id}',
			path: {
				id
			},
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Referral Allocation
	 * Delete an referral_allocation.
	 * @returns Message Successful Response
	 * @throws ApiError
	 */
	public static deleteReferralAllocation(data: TDataDeleteReferralAllocation): CancelablePromise<Message> {
		const {
id,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/referrals_allocations/{id}',
			path: {
				id
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataReadReferrals = {
                limit?: number
skip?: number
                
            }
export type TDataCreateReferral = {
                requestBody: ReferralCreate
                
            }
export type TDataReadReferral = {
                id: number
                
            }
export type TDataUpdateReferral = {
                id: number
requestBody: ReferralUpdate
                
            }
export type TDataDeleteReferral = {
                id: number
                
            }

export class ReferralsService {

	/**
	 * Read Referrals
	 * Retrieve referrals.
	 * @returns ReferralsPublic Successful Response
	 * @throws ApiError
	 */
	public static readReferrals(data: TDataReadReferrals = {}): CancelablePromise<ReferralsPublic> {
		const {
limit = 100,
skip = 0,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/referrals/',
			query: {
				skip, limit
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Referral
	 * Create new referral.
	 * @returns ReferralPublic Successful Response
	 * @throws ApiError
	 */
	public static createReferral(data: TDataCreateReferral): CancelablePromise<ReferralPublic> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/referrals/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read Referral
	 * Get referral by ID.
	 * @returns ReferralPublic Successful Response
	 * @throws ApiError
	 */
	public static readReferral(data: TDataReadReferral): CancelablePromise<ReferralPublic> {
		const {
id,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/referrals/{id}',
			path: {
				id
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Update Referral
	 * Update an referral.
	 * @returns ReferralPublic Successful Response
	 * @throws ApiError
	 */
	public static updateReferral(data: TDataUpdateReferral): CancelablePromise<ReferralPublic> {
		const {
id,
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'PUT',
			url: '/api/v1/referrals/{id}',
			path: {
				id
			},
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Referral
	 * Delete an referral.
	 * @returns Message Successful Response
	 * @throws ApiError
	 */
	public static deleteReferral(data: TDataDeleteReferral): CancelablePromise<Message> {
		const {
id,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/referrals/{id}',
			path: {
				id
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataReadSourceRateRates = {
                limit?: number
skip?: number
                
            }
export type TDataCreateSourceRateRate = {
                requestBody: Source_RateCreate
                
            }
export type TDataReadSourceRateRate = {
                id: number
                
            }
export type TDataUpdateSourceRate = {
                id: number
requestBody: Source_RateUpdate
                
            }
export type TDataDeleteSourceRate = {
                id: number
                
            }

export class SourceRatesService {

	/**
	 * Read Source Rate Rates
	 * Retrieve source_rate_rates.
	 * @returns Source_RatesPublic Successful Response
	 * @throws ApiError
	 */
	public static readSourceRateRates(data: TDataReadSourceRateRates = {}): CancelablePromise<Source_RatesPublic> {
		const {
limit = 100,
skip = 0,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/source_rates/',
			query: {
				skip, limit
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Source Rate Rate
	 * Create new source_rate.
	 * @returns Source_RatePublic Successful Response
	 * @throws ApiError
	 */
	public static createSourceRateRate(data: TDataCreateSourceRateRate): CancelablePromise<Source_RatePublic> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/source_rates/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read Source Rate Rate
	 * Get source_rate_rate by ID.
	 * @returns Source_RatePublic Successful Response
	 * @throws ApiError
	 */
	public static readSourceRateRate(data: TDataReadSourceRateRate): CancelablePromise<Source_RatePublic> {
		const {
id,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/source_rates/{id}',
			path: {
				id
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Update Source Rate
	 * Update an source_rate.
	 * @returns Source_RatePublic Successful Response
	 * @throws ApiError
	 */
	public static updateSourceRate(data: TDataUpdateSourceRate): CancelablePromise<Source_RatePublic> {
		const {
id,
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'PUT',
			url: '/api/v1/source_rates/{id}',
			path: {
				id
			},
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Source Rate
	 * Delete an source_rate.
	 * @returns Message Successful Response
	 * @throws ApiError
	 */
	public static deleteSourceRate(data: TDataDeleteSourceRate): CancelablePromise<Message> {
		const {
id,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/source_rates/{id}',
			path: {
				id
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataReadSupplierRateRates = {
                limit?: number
skip?: number
                
            }
export type TDataCreateSupplierRateRate = {
                requestBody: Supplier_RateCreate
                
            }
export type TDataReadSupplierRateRate = {
                id: number
                
            }
export type TDataUpdateSupplierRate = {
                id: number
requestBody: Supplier_RateUpdate
                
            }
export type TDataDeleteSupplierRate = {
                id: number
                
            }

export class SupplierRatesService {

	/**
	 * Read Supplier Rate Rates
	 * Retrieve supplier_rate_rates.
	 * @returns Supplier_RatesPublic Successful Response
	 * @throws ApiError
	 */
	public static readSupplierRateRates(data: TDataReadSupplierRateRates = {}): CancelablePromise<Supplier_RatesPublic> {
		const {
limit = 100,
skip = 0,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/supplier_rates/',
			query: {
				skip, limit
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Supplier Rate Rate
	 * Create new supplier_rate.
	 * @returns Supplier_RatePublic Successful Response
	 * @throws ApiError
	 */
	public static createSupplierRateRate(data: TDataCreateSupplierRateRate): CancelablePromise<Supplier_RatePublic> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/supplier_rates/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read Supplier Rate Rate
	 * Get supplier_rate_rate by ID.
	 * @returns Supplier_RatePublic Successful Response
	 * @throws ApiError
	 */
	public static readSupplierRateRate(data: TDataReadSupplierRateRate): CancelablePromise<Supplier_RatePublic> {
		const {
id,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/supplier_rates/{id}',
			path: {
				id
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Update Supplier Rate
	 * Update an supplier_rate.
	 * @returns Supplier_RatePublic Successful Response
	 * @throws ApiError
	 */
	public static updateSupplierRate(data: TDataUpdateSupplierRate): CancelablePromise<Supplier_RatePublic> {
		const {
id,
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'PUT',
			url: '/api/v1/supplier_rates/{id}',
			path: {
				id
			},
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Supplier Rate
	 * Delete an supplier_rate.
	 * @returns Message Successful Response
	 * @throws ApiError
	 */
	public static deleteSupplierRate(data: TDataDeleteSupplierRate): CancelablePromise<Message> {
		const {
id,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/supplier_rates/{id}',
			path: {
				id
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataReadVehGroups = {
                limit?: number
skip?: number
                
            }
export type TDataCreateVehGroup = {
                requestBody: Veh_GroupCreate
                
            }
export type TDataReadVehGroup = {
                id: number
                
            }
export type TDataUpdateVehGroup = {
                id: number
requestBody: Veh_GroupUpdate
                
            }
export type TDataDeleteVehGroup = {
                id: number
                
            }

export class VehGroupsService {

	/**
	 * Read Veh Groups
	 * Retrieve veh_groups.
	 * @returns Veh_GroupsPublic Successful Response
	 * @throws ApiError
	 */
	public static readVehGroups(data: TDataReadVehGroups = {}): CancelablePromise<Veh_GroupsPublic> {
		const {
limit = 100,
skip = 0,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/veh_groups/',
			query: {
				skip, limit
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Veh Group
	 * Create new veh_group.
	 * @returns Veh_GroupPublic Successful Response
	 * @throws ApiError
	 */
	public static createVehGroup(data: TDataCreateVehGroup): CancelablePromise<Veh_GroupPublic> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/veh_groups/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read Veh Group
	 * Get veh_group by ID.
	 * @returns Veh_GroupPublic Successful Response
	 * @throws ApiError
	 */
	public static readVehGroup(data: TDataReadVehGroup): CancelablePromise<Veh_GroupPublic> {
		const {
id,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/veh_groups/{id}',
			path: {
				id
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Update Veh Group
	 * Update an veh_group.
	 * @returns Veh_GroupPublic Successful Response
	 * @throws ApiError
	 */
	public static updateVehGroup(data: TDataUpdateVehGroup): CancelablePromise<Veh_GroupPublic> {
		const {
id,
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'PUT',
			url: '/api/v1/veh_groups/{id}',
			path: {
				id
			},
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Veh Group
	 * Delete an veh_group.
	 * @returns Message Successful Response
	 * @throws ApiError
	 */
	public static deleteVehGroup(data: TDataDeleteVehGroup): CancelablePromise<Message> {
		const {
id,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/veh_groups/{id}',
			path: {
				id
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}

export type TDataReadAuthorities = {
                limit?: number
skip?: number
                
            }
export type TDataCreateAuthority = {
                requestBody: AuthorityCreate
                
            }
export type TDataReadAuthority = {
                id: number
                
            }
export type TDataUpdateAuthority = {
                id: number
requestBody: AuthorityUpdate
                
            }
export type TDataDeleteAuthority = {
                id: number
                
            }

export class AuthoritiesService {

	/**
	 * Read Authorities
	 * Retrieve authorities.
	 * @returns AuthoritiesPublic Successful Response
	 * @throws ApiError
	 */
	public static readAuthorities(data: TDataReadAuthorities = {}): CancelablePromise<AuthoritiesPublic> {
		const {
limit = 100,
skip = 0,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/authorities/',
			query: {
				skip, limit
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Create Authority
	 * Create new authority.
	 * @returns AuthorityPublic Successful Response
	 * @throws ApiError
	 */
	public static createAuthority(data: TDataCreateAuthority): CancelablePromise<AuthorityPublic> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/authorities/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Read Authority
	 * Get authority by ID.
	 * @returns AuthorityPublic Successful Response
	 * @throws ApiError
	 */
	public static readAuthority(data: TDataReadAuthority): CancelablePromise<AuthorityPublic> {
		const {
id,
} = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/authorities/{id}',
			path: {
				id
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Update Authority
	 * Update an authority.
	 * @returns AuthorityPublic Successful Response
	 * @throws ApiError
	 */
	public static updateAuthority(data: TDataUpdateAuthority): CancelablePromise<AuthorityPublic> {
		const {
id,
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'PUT',
			url: '/api/v1/authorities/{id}',
			path: {
				id
			},
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

	/**
	 * Delete Authority
	 * Delete an authority.
	 * @returns Message Successful Response
	 * @throws ApiError
	 */
	public static deleteAuthority(data: TDataDeleteAuthority): CancelablePromise<Message> {
		const {
id,
} = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/api/v1/authorities/{id}',
			path: {
				id
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}

}


export class RequestsService {

	/**
	 * Create Referral
	 * Create new request.
	 * @returns unknown Successful Response
	 * @throws ApiError
	 */
	public static createReferral(data: TDataCreateReferral): CancelablePromise<unknown> {
		const {
requestBody,
} = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/requests/',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				422: `Validation Error`,
			},
		});
	}

}