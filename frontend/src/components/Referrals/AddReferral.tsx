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

import { type ApiError, type ReferralCreate, ReferralsService } from "../../client"
import useCustomToast from "../../hooks/useCustomToast"

interface AddReferralProps {
  isOpen: boolean
  onClose: () => void
}

const AddReferral = ({ isOpen, onClose }: AddReferralProps) => {
  const queryClient = useQueryClient()
  const showToast = useCustomToast()
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<ReferralCreate>({
    mode: "onBlur",
    criteriaMode: "all",
    defaultValues: {
      //claim_id: ,
      //description: "",
    },
  })

  const mutation = useMutation({
    mutationFn: (data: ReferralCreate) =>
      ReferralsService.createReferral({ requestBody: data }),
    onSuccess: () => {
      showToast("Success!", "Referral created successfully.", "success")
      reset()
      onClose()
    },
    onError: (err: ApiError) => {
      const errDetail = (err.body as any)?.detail
      showToast("Something went wrong.", `${errDetail}`, "error")
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["referrals"] })
    },
  })

  const onSubmit: SubmitHandler<ReferralCreate> = (data) => {
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
          <ModalHeader>Add Referral</ModalHeader>
          <ModalCloseButton />
          <ModalBody pb={6}>
            <FormControl isRequired isInvalid={!!errors.source_id}>
              <FormLabel htmlFor="source_id">Source ID</FormLabel>
              <Input
                id="source_id"
                {...register("source_id", {
                  required: "Source ID is required.",
                })}
                placeholder="Source ID"
                type="text"
              />
              {errors.source_id && (
                <FormErrorMessage>{errors.source_id.message}</FormErrorMessage>
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

export default AddReferral
