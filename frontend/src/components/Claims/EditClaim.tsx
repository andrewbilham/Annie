import {
  Button,
  FormControl,
  FormErrorMessage,
  FormLabel,
  Input,
  Modal,
  ModalBody,
  ModalCloseButton,
  ModalContent,
  ModalFooter,
  ModalHeader,
  ModalOverlay,
} from "@chakra-ui/react"
import { useMutation, useQueryClient } from "@tanstack/react-query"
import { type SubmitHandler, useForm } from "react-hook-form"

import {
  type ApiError,
  type ClaimPublic,
  type ClaimUpdate,
  ClaimsService,
} from "../../client"
import useCustomToast from "../../hooks/useCustomToast"

interface EditClaimProps {
  claim: ClaimPublic
  isOpen: boolean
  onClose: () => void
}

const EditClaim = ({ claim, isOpen, onClose }: EditClaimProps) => {
  const queryClient = useQueryClient()
  const showToast = useCustomToast()
  const {
    register,
    handleSubmit,
    reset,
    formState: { isSubmitting, errors, isDirty },
  } = useForm<ClaimUpdate>({
    mode: "onBlur",
    criteriaMode: "all",
    defaultValues: claim,
  })

  const mutation = useMutation({
    mutationFn: (data: ClaimUpdate) =>
      ClaimsService.updateClaim({ id: claim.id, requestBody: data }),
    onSuccess: () => {
      showToast("Success!", "Claim updated successfully.", "success")
      onClose()
    },
    onError: (err: ApiError) => {
      const errDetail = (err.body as any)?.detail
      showToast("Something went wrong.", `${errDetail}`, "error")
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["claims"] })
    },
  })

  const onSubmit: SubmitHandler<ClaimUpdate> = async (data) => {
    mutation.mutate(data)
  }

  const onCancel = () => {
    reset()
    onClose()
  }

  return (
    <>
      <Modal
        isOpen={isOpen}
        onClose={onClose}
        size={{ base: "sm", md: "md" }}
        isCentered
      >
        <ModalOverlay />
        <ModalContent as="form" onSubmit={handleSubmit(onSubmit)}>
          <ModalHeader>Edit Claim</ModalHeader>
          <ModalCloseButton />
          <ModalBody pb={6}>
            <FormControl isInvalid={!!errors.client_firstname}>
              <FormLabel htmlFor="client_firstname">First Name</FormLabel>
              <Input
                id="client_firstname"
                {...register("client_firstname", {
                  required: "First Name is required",
                })}
                type="text"
              />
              {errors.client_firstname && (
                <FormErrorMessage>{errors.client_firstname.message}</FormErrorMessage>
              )}
            </FormControl>
            {/* <FormControl mt={4}>
              <FormLabel htmlFor="description">Description</FormLabel>
              <Input
                id="description"
                {...register("description")}
                placeholder="Description"
                type="text"
              />
            </FormControl> */}
          </ModalBody>
          <ModalFooter gap={3}>
            <Button
              variant="primary"
              type="submit"
              isLoading={isSubmitting}
              isDisabled={!isDirty}
            >
              Save
            </Button>
            <Button onClick={onCancel}>Cancel</Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>
  )
}

export default EditClaim
