/**
  Spring 에서 Post 요청 데이터 받는 방법
  - @RequestBody (DTO)
 */


/**
  Request 의 requestBody 를 받는 방법
  POST http://localhost:8080/api/v1/member
 */

// 방법 1 - request body Map(dict) 형식으로 받기
@PostMapping(value = "/member")
public String postMember(@RequestBody Map<String, Object> postData) {
  StringBuilder sb = new StringBuilder();

  postData.entrySet().forEach(map -> {
    sb.append(map.getKey() + ":" + map.getValue() + "\n");
  })

  return sb.toString();
}


// 방법 2 - request body DTO 형식으로 받기
@PostMapping(value = "/member2")
public String postMemberDto(@RequestBody MemberDTO memberDTO) {
  return memberDTO.toString();
}



