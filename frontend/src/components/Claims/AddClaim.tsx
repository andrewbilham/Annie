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

import { type ApiError, type ClaimCreate, ClaimsService } from "../../client"
import useCustomToast from "../../hooks/useCustomToast"

interface AddClaimProps {
  isOpen: boolean
  onClose: () => void
}

const AddClaim = ({ isOpen, onClose }: AddClaimProps) => {
  const queryClient = useQueryClient()
  const showToast = useCustomToast()
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<ClaimCreate>({
    mode: "onBlur",
    criteriaMode: "all",
    defaultValues: {
      client_firstname: "",
      //description: "",
    },
  })

  const mutation = useMutation({
    mutationFn: (data: ClaimCreate) =>
      ClaimsService.createClaim({ requestBody: data }),
    onSuccess: () => {
      showToast("Success!", "Claim created successfully.", "success")
      reset()
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

  const onSubmit: SubmitHandler<ClaimCreate> = (data) => {
    mutation.mutate(data)
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
          <ModalHeader>Add Claim</ModalHeader>
          <ModalCloseButton />
          <ModalBody pb={6}>
            <FormControl isRequired isInvalid={!!errors.client_firstname}>
              <FormLabel htmlFor="client_firstname">First Name</FormLabel>
              <Input
                id="client_firstname"
                {...register("client_firstname", {
                  required: "First Name is required.",
                })}
                placeholder="First Name"
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
            <Button variant="primary" type="submit" isLoading={isSubmitting}>
              Save
            </Button>
            <Button onClick={onClose}>Cancel</Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>
  )
}

export default AddClaim
