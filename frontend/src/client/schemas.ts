export const $AuthoritiesPublic = {
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'AuthorityPublic',
	},
	isRequired: true,
},
		count: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $AuthorityCreate = {
	properties: {
		name: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $AuthorityPublic = {
	properties: {
		name: {
	type: 'string',
	isRequired: true,
},
		id: {
	type: 'number',
	isRequired: true,
},
		owner_id: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $AuthorityUpdate = {
	properties: {
		name: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $Body_login_login_access_token = {
	properties: {
		grant_type: {
	type: 'any-of',
	contains: [{
	type: 'string',
	pattern: 'password',
}, {
	type: 'null',
}],
},
		username: {
	type: 'string',
	isRequired: true,
},
		password: {
	type: 'string',
	isRequired: true,
},
		scope: {
	type: 'string',
	default: '',
},
		client_id: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		client_secret: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $Circs_GroupCreate = {
	properties: {
		group: {
	type: 'string',
	isRequired: true,
},
		desc: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $Circs_GroupPublic = {
	properties: {
		group: {
	type: 'string',
	isRequired: true,
},
		desc: {
	type: 'string',
	isRequired: true,
},
		id: {
	type: 'number',
	isRequired: true,
},
		owner_id: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $Circs_GroupUpdate = {
	properties: {
		group: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		desc: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $Circs_GroupsPublic = {
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'Circs_GroupPublic',
	},
	isRequired: true,
},
		count: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $ClaimCreate = {
	properties: {
		client_firstname: {
	type: 'string',
	isRequired: true,
},
		client_lastname: {
	type: 'string',
	isRequired: true,
},
		authority_id: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $ClaimPublic = {
	properties: {
		client_firstname: {
	type: 'string',
	isRequired: true,
},
		client_lastname: {
	type: 'string',
	isRequired: true,
},
		authority_id: {
	type: 'number',
	isRequired: true,
},
		id: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $ClaimUpdate = {
	properties: {
		client_firstname: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		client_lastname: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		authority_id: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $ClaimsPublic = {
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'ClaimPublic',
	},
	isRequired: true,
},
		count: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $HTTPValidationError = {
	properties: {
		detail: {
	type: 'array',
	contains: {
		type: 'ValidationError',
	},
},
	},
} as const;

export const $ItemCreate = {
	properties: {
		title: {
	type: 'string',
	isRequired: true,
},
		description: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $ItemPublic = {
	properties: {
		title: {
	type: 'string',
	isRequired: true,
},
		description: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		id: {
	type: 'number',
	isRequired: true,
},
		owner_id: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $ItemUpdate = {
	properties: {
		title: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		description: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $ItemsPublic = {
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'ItemPublic',
	},
	isRequired: true,
},
		count: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $Message = {
	properties: {
		message: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $NewPassword = {
	properties: {
		token: {
	type: 'string',
	isRequired: true,
},
		new_password: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $ReferralCreate = {
	properties: {
		source_id: {
	type: 'number',
	isRequired: true,
},
		claim_id: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $ReferralPublic = {
	properties: {
		source_id: {
	type: 'number',
	isRequired: true,
},
		claim_id: {
	type: 'number',
	isRequired: true,
},
		id: {
	type: 'number',
	isRequired: true,
},
		owner_id: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $ReferralUpdate = {
	properties: {
		source_id: {
	type: 'any-of',
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
		claim_id: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $Referral_AllocationCreate = {
	properties: {
		Source: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $Referral_AllocationPublic = {
	properties: {
		Source: {
	type: 'string',
	isRequired: true,
},
		id: {
	type: 'number',
	isRequired: true,
},
		owner_id: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $Referral_AllocationUpdate = {
	properties: {
		Source: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $Referral_AllocationsPublic = {
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'Referral_AllocationPublic',
	},
	isRequired: true,
},
		count: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $ReferralsPublic = {
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'ReferralPublic',
	},
	isRequired: true,
},
		count: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $RequestCreate = {
	properties: {
		type: {
	type: 'string',
	isRequired: true,
},
		source_id: {
	type: 'number',
	isRequired: true,
},
		client_firstname: {
	type: 'string',
	isRequired: true,
},
		client_lastname: {
	type: 'string',
	isRequired: true,
},
		authority_id: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $SourceCreate = {
	properties: {
		source_name: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $SourcePublic = {
	properties: {
		source_name: {
	type: 'string',
	isRequired: true,
},
		id: {
	type: 'number',
	isRequired: true,
},
		owner_id: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $SourceUpdate = {
	properties: {
		source_name: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $Source_RateCreate = {
	properties: {
		rate: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $Source_RatePublic = {
	properties: {
		rate: {
	type: 'number',
	isRequired: true,
},
		id: {
	type: 'number',
	isRequired: true,
},
		owner_id: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $Source_RateUpdate = {
	properties: {
		rate: {
	type: 'any-of',
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $Source_RatesPublic = {
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'Source_RatePublic',
	},
	isRequired: true,
},
		count: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $SourcesPublic = {
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'SourcePublic',
	},
	isRequired: true,
},
		count: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $SupplierCreate = {
	properties: {
		name: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $SupplierPublic = {
	properties: {
		name: {
	type: 'string',
	isRequired: true,
},
		id: {
	type: 'number',
	isRequired: true,
},
		owner_id: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $SupplierUpdate = {
	properties: {
		name: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $Supplier_RateCreate = {
	properties: {
		rate: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $Supplier_RatePublic = {
	properties: {
		rate: {
	type: 'number',
	isRequired: true,
},
		id: {
	type: 'number',
	isRequired: true,
},
		owner_id: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $Supplier_RateUpdate = {
	properties: {
		rate: {
	type: 'any-of',
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $Supplier_RatesPublic = {
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'Supplier_RatePublic',
	},
	isRequired: true,
},
		count: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $SuppliersPublic = {
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'SupplierPublic',
	},
	isRequired: true,
},
		count: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $Token = {
	properties: {
		access_token: {
	type: 'string',
	isRequired: true,
},
		token_type: {
	type: 'string',
	default: 'bearer',
},
	},
} as const;

export const $UpdatePassword = {
	properties: {
		current_password: {
	type: 'string',
	isRequired: true,
},
		new_password: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $UserCreate = {
	properties: {
		email: {
	type: 'string',
	isRequired: true,
},
		is_active: {
	type: 'boolean',
	default: true,
},
		is_superuser: {
	type: 'boolean',
	default: false,
},
		full_name: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		password: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $UserPublic = {
	properties: {
		email: {
	type: 'string',
	isRequired: true,
},
		is_active: {
	type: 'boolean',
	default: true,
},
		is_superuser: {
	type: 'boolean',
	default: false,
},
		full_name: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		id: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $UserRegister = {
	properties: {
		email: {
	type: 'string',
	isRequired: true,
},
		password: {
	type: 'string',
	isRequired: true,
},
		full_name: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $UserUpdate = {
	properties: {
		email: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		is_active: {
	type: 'boolean',
	default: true,
},
		is_superuser: {
	type: 'boolean',
	default: false,
},
		full_name: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		password: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $UserUpdateMe = {
	properties: {
		full_name: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		email: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $UsersPublic = {
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'UserPublic',
	},
	isRequired: true,
},
		count: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $ValidationError = {
	properties: {
		loc: {
	type: 'array',
	contains: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'number',
}],
},
	isRequired: true,
},
		msg: {
	type: 'string',
	isRequired: true,
},
		type: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $Veh_GroupCreate = {
	properties: {
		group: {
	type: 'string',
	isRequired: true,
},
		desc: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $Veh_GroupPublic = {
	properties: {
		group: {
	type: 'string',
	isRequired: true,
},
		desc: {
	type: 'string',
	isRequired: true,
},
		id: {
	type: 'number',
	isRequired: true,
},
		owner_id: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $Veh_GroupUpdate = {
	properties: {
		group: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		desc: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $Veh_GroupsPublic = {
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'Veh_GroupPublic',
	},
	isRequired: true,
},
		count: {
	type: 'number',
	isRequired: true,
},
	},
} as const;